1. Go to your instance overview page
2. Identify the instance's internal and external DNS.
3. Try to resolve both of them from within the instance, which IP did you get?


<details>
  <summary>
     Solution
  </summary>
    
    ```bash
    dig internal-dns-name
    dig external-dns-name
    ```

Typically, you will find that the internal DNS resolves to the private IP address of the instance, while the external DNS resolves to the public IP address associated with the instance. 

</details>
