
1. Open the [Step Functions page](https://console.aws.amazon.com/lambda/home#/stepfunctions) of the Lambda console\.
2. Choose **Create state machine**.
3. Choose **Write your workflow in code** and edit the JSON in the **Definition** pane as follows:
    1. Copy and paste `face-blur-lambdas/state_machine.json`
    2. Change `<check-rekognition-job-status ARN>`, `<get-rekognized-faces ARN>` and `<blur-faces ARN>` according to the corresponding Lambda functions ARN.
4. Click **Next**.
5. Enter a unique name to your state machine.
6. Under **Logging**, enable ALL logging.
7. Choose **Create state machine**.

8. Add the following env var to the "face-detection" function (the first one):
   `STATE_MACHINE_ARN=<state-machine-ARN>`
