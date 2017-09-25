# faas-azure-cli
Python example using the Azure-Cli in a function. This example returns the Subscription Id of the first subscription in the account list.

```
$ git clone https://github.com/faas-and-furious/faas-azure-cli
$ cd faas-azure-cli
```
Azure Service Principle

You will need to create a SPN in azure and update the following lines in `faas-azure-cli.yml`. Follow this link to create a SPN -- [Portal: Create SPN](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal)

```
username: <spn client id>
password: <spn client seceret>
tenant: <aad tenant id>
```

Now build and deploy:

```
$ faas-cli build -f faas-azure-cli.yml
$ faas-cli push -f faas-azure-cli.yml
$ faas-cli deploy -f faas-azure-cli.yml
```

Try it out:

```
$ curl -X POST localhost:8080/function/faasazurecli
```

