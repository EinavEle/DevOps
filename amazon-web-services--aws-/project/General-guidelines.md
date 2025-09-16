
- Throughout the exercise you should not use IAM user credentials explicitly, instead, **use IAM roles** with the required permissions and attach them on your EC2 instances.
- Test your application under load, observe the `BacklogPerInstance` metric values in CloudWatch. Watch how CloudWatch firing a **scale out alarm** which increasing the desired capacity of your AutoscalingGroup, and when the `BacklogPerInstance` value is low, watch the **scale in alarm** fired.
- You are highly encouraged to improve the bot logic, add functionality etc...
