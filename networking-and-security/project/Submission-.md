Push your solution branch and make sure you pass the automatic tests in GitHub actions. 


**Note**: Your EC2 instances should be running while the automated test is performed. **Don't forget to turn off the machines when you're done**.

**Run tests locally** (recommended)

You are highly encouraged to test your solution locally before pushing it to GitHub. To run tests, `cd` to `networking_project/test` and execute the relevant test file:

**Test bastion**

```bash
export PUBLIC_EC2_IP=<fill me>
export PRIVATE_EC2_IP=<fill me>
export KEY_PATH=<fill me>
bash test_bastion_locally.sh
```

**Test keys rotation**

```bash
export PUBLIC_EC2_IP=<fill me>
export PRIVATE_EC2_IP=<fill me>
export KEY_PATH=<fill me>
bash test_rotation_locally.sh
```



#### Good luck!