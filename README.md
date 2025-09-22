# OPA Service Helm Chart

## Installation

### Using the Helm repository hosted in GitHub Pages

First, add the Helm repository:

```shell
$ helm repo add opa-service-helm https://tefiros.github.io/opa-service-helm/
```

Then, install the Helm Chart:

```shell
$ helm install opa-service opa-service-helm/opa-service
```

The chart will be installed using the default values. Use the provided [`values.yaml`](https://github.com/candil-data-fabric/data-security-service-helm/blob/develop/values.yaml) file in this repository as template to upgrade the installation with your desired parameters:

```shell
$ helm upgrade opa-service -f myvalues.yaml
```

To uninstall the Helm Chart, run the following command:

```shell
$ helm uninstall opa-service
```

### Cloning this repository

First, clone the repository:

```shell
$ git clone https://github.com/tefiros/opa-service-helm.git
```

Once cloned, edit the [`values.yaml`](https://github.com/candil-data-fabric/data-security-service-helm/blob/develop/values.yaml) file to match your deployment needs and run the following command:

```shell
$ helm install opa-service .
```

To uninstall the Helm Chart, run the following command:

```shell
$ helm uninstall opa-service
```
