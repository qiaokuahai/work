### 总述
```
Chart文件中，比较重要的文件可以认为是5个：Chart.yaml，values.yaml，templates下的：configmap.yaml，deployment.yaml，service.yaml
```
### Chart.ymal
```
apiVersion: # K8s API版本，目前是用的是“v1”（必需）
name: # 工程的包名（必需）
version: # Chart版本号，需要符合 SemVer 2：http://semver.org/(语义化版本规范)（必需）
kubeVersion: # 一系列兼容的Kubernetes版本（可选）
description: # Chart描述，通常用一句话描述项目（可选）
keywords:
  - # 有关此项目的关键字列表，便于检索（可选）
home: # 项目主页URL（可选）
sources:
  - # 指向此项目源代码的URL列表（可选）
maintainers: # 维护人员信息(可选)
  - name: # 维护者姓名（每个维护者必须填写）
    email: # 维护者电子邮件（每个维护者可选）
    url: # 维护者URL（每个维护者可选）
engine: gotpl # 模板引擎名称（可选，默认为gotpl）
icon: # 要用作图标的SVG或PNG图像的URL（可选）
appVersion: # 包含的应用程序版本（可选）。这不必是SemVer
deprecated: # 此“chart”是否已弃用（可选，布尔值）
tillerVersion: 此“chart”所需的“Tiller”版本。这应该表示为SemVer范围：“>2.0.0”（可选）
```

### Values.yaml
```
# Default values for mychart.
# This is a yaml-formatted file.
# Declare variables to be passed into your templates.
replicaCount: 1
image:
  repository: nginx
  tag: stable
  pullPolicy: IfNotPresent
service:
  name: nginx
  type: ClusterIP
  externalPort: 80
  internalPort: 80
resources:
  limits:
    cpu: 100m
    memory: 128Mi
  requests:
    cpu: 100m
    memory: 128Mi
```

### Deployment.yaml
```
apiVersion: extensions/v1
kind: Deployment
metadata:
  name: {{ template "fullname" . }}
  labels:
    chart: "{{ .Chart.Name }}-{{ .Chart.Version | replace "+" "_" }}"
spec:
  replicas: {{ .Values.replicaCount }}
  template:
    metadata:
      labels:
        app: {{ template "fullname" . }}
    spec:
      containers:
      - name: {{ .Chart.Name }}
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
        imagePullPolicy: {{ .Values.image.pullPolicy }}
        ports:
        - containerPort: {{ .Values.service.internalPort }}
        livenessProbe:
          httpGet:
            path: /
            port: {{ .Values.service.internalPort }}
        readinessProbe:
          httpGet:
            path: /
            port: {{ .Values.service.internalPort }}
        resources:
{{ toyaml .Values.resources | indent 12 }}
```


