Take a look on the created permission JSON, identify the components 


<details>
  <summary>
     Solution
  </summary>

```JSON
    {
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "s3:*",  // Allowed actions on Amazon S3 resources
        "s3-object-lambda:*"  // Allowed actions on S3 Object Lambda resources
      ],
      "Resource" : "*"  // Allowed resource - in this case, all resources
    }
  ]
}
```


- `Version`: Denotes the version of the policy language being used.
- `Statement`: An array of policy statements, each defining a permission rule.
- `Effect`: Specifies whether the statement allows or denies access ("Allow" in this case).
- `Action`: Lists the actions allowed ("s3:" for all S3 actions, "s3-object-lambda:" for all S3 Object Lambda  actions).
- `Resource`: Specifies the resource to which the actions apply ("*" signifies all resources).

This policy allows any action (`s3:*`) and any action on S3 Object Lambda (`s3-object-lambda:*`) for any resource (`*`) because of the `Allow` effect.


</details>


