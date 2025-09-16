
## Create an SNS topic

1. Sign in to the Amazon SNS console at https://console.aws.amazon.com/sns/home.
1. Do one of the following:

    - If no topics have ever been created under your AWS account before, read the description of Amazon SNS on the home page.
    - If topics have been created under your AWS account before, on the navigation panel, choose **Topics**.

1. On the **Topics** page, choose **Create topic**.
1. On the Create topic page, in the Details section, do the following:

    - For **Type**, choose a **Standard** type.
    - Enter a **Name** for the topic. E.g. `jobs-completion-topic`

1. Enter a **Display nam**e for the topic.
1. To configure how Amazon SNS retries failed message delivery attempts, expand the **Delivery retry policy (HTTP/S)** section. For more information, see [Amazon SNS message delivery retries](https://docs.aws.amazon.com/sns/latest/dg/sns-message-delivery-retries.html).
2. Choose **Create** topic.


## Subscribe to a topic, confirm the subscription, and `ngrok`

To receive messages published to a topic, you must subscribe an HTTP **endpoint** to the topic.
After you subscribe your endpoint, SNS will send a subscription confirmation message to the endpoint.

Let's quickly review how it's done in the code (under `youtube_subtitles_v4/fronetend/app.py`):

1. ```python
    response = sns_client.subscribe(
        TopicArn=topic_arn,
        Protocol='https',
        Endpoint=server_endpoint
    )
    ```

In this section, the `sns_client.subscribe()` method is used to subscribe the Flask server (`server_endpoint`) to the SNS topic (`topic_arn`). 
This code sets up the subscription, specifying that the protocol to be used is HTTPS.

2. ```python
    @app.route('/job_update', methods=['POST'])
    def job_update():
        data = json.loads(request.get_data().decode())
        if 'Type' in data and data['Type'] == 'SubscriptionConfirmation':
            sns_client.confirm_subscription(TopicArn=data['TopicArn'], Token=data['Token'])
            logger.info(f"Subscribed successfully with SubscriptionArn: {subscription_arn}")
        else:
            # ... (job_id processing logic)
        return "OK"
    ```

This Flask route, `/job_update`, serves as the endpoint to handle subscription updates from the SNS topic.
When a `POST` request is received here, the json data is parsed, and it's checked whether the Type field is set to `SubscriptionConfirmation`.
If it is, the Flask server confirms the subscription by calling `sns_client.confirm_subscription()` with the provided `TopicArn` and `Token`.
This confirms the subscription and logs the successful confirmation.

### `ngrok` introducing

Now, since you run the flask webserver **locally**, and SNS needs to send a subscription confirmation message, 
there's a challenge here. Your flask server is not accessible from the internet.

This is where **ngrok** comes in to solve the problem.

[Ngrok](https://ngrok.com/) creates a secure tunnel between the local machine and a public URL provided by Ngrok.
It exposes the local server to the internet, allowing AWS SNS servers to reach your flask webserver which runs locally.

Sign-up for the Ngrok service (or any another tunneling service to your choice), then install the `ngrok` agent as [described here](https://ngrok.com/docs/getting-started/#step-2-install-the-ngrok-agent). 

Authenticate your ngrok agent. You only have to do this once:

```bash
ngrok config add-authtoken <your-authtoken>
```

Since the flask webserver will be listening on port `8080`, start ngrok by running the following command:

```bash
ngrok http 8080
```

Your public URL is the URL specified in the `Forwarding` line (e.g. `https://16ae-2a06-c701-4501-3a00-ecce-30e9-3e61-3069.ngrok-free.app`).
Don't forget to change the value of `YOUR_SERVER_URL` accordingly. 
