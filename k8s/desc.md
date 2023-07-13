### 展示 pod replicaSet deployment关系
```
--- show pod
[root@VM_0_17_centos ~]# kubectl describe pod mq-svc-5b96bf78d9-brpjw
Name:           mq-svc-5b96bf78d9-brpjw
Namespace:      default
Node:           10.0.0.17/10.0.0.17
Start Time:     Fri, 17 Aug 2018 17:24:44 +0800
Labels:         pod-template-hash=1652693485
                qcloud-app=mq-svc
Annotations:    <none>
Status:         Running
IP:             172.16.0.39
Controlled By:  ReplicaSet/mq-svc-5b96bf78d9
Containers:
  queue-mq:
    Container ID:   docker://700cdc55c111a413faaa8cabb8680009d2663701ccbe84b8a50ea6e6fe1d538c
    Image:          rabbitmq:management
    Image ID:       docker-pullable://rabbitmq@sha256:0b36ea1a8df9e53228aaeee277680de2cc97c7d675bc2d5dbe1cc9e3836a9d9f
    Port:           <none>
    Host Port:      <none>
    State:          Running
      Started:      Fri, 17 Aug 2018 17:24:49 +0800
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     500m
      memory:  1Gi
    Requests:
      cpu:        250m
      memory:     256Mi
    Environment:  <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-vzhz4 (ro)
Conditions:
  Type           Status
  Initialized    True 
  Ready          True 
  PodScheduled   True 
Volumes:
  default-token-vzhz4:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-vzhz4
    Optional:    false
QoS Class:       Burstable
Node-Selectors:  <none>
Tolerations:     <none>
Events:
  Type    Reason                 Age   From                Message
  ----    ------                 ----  ----                -------
  Normal  Scheduled              51m   default-scheduler   Successfully assigned mq-svc-5b96bf78d9-brpjw to 10.0.0.17
  Normal  SuccessfulMountVolume  51m   kubelet, 10.0.0.17  MountVolume.SetUp succeeded for volume "default-token-vzhz4"
  Normal  Pulling                51m   kubelet, 10.0.0.17  pulling image "rabbitmq:management"
  Normal  Pulled                 51m   kubelet, 10.0.0.17  Successfully pulled image "rabbitmq:management"
  Normal  Created                51m   kubelet, 10.0.0.17  Created container
  Normal  Started                51m   kubelet, 10.0.0.17  Started container


--- show rs
[root@VM_0_17_centos ~]# kubectl describe rs mq-svc-5b96bf78d9
Name:           mq-svc-5b96bf78d9
Namespace:      default
Selector:       pod-template-hash=1652693485,qcloud-app=mq-svc
Labels:         pod-template-hash=1652693485
                qcloud-app=mq-svc
Annotations:    deployment.changecourse=Updating
                deployment.kubernetes.io/desired-replicas=1
                deployment.kubernetes.io/max-replicas=2
                deployment.kubernetes.io/revision=2
                description=Service based on rabbitmq.
Controlled By:  Deployment/mq-svc
Replicas:       1 current / 1 desired
Pods Status:    1 Running / 0 Waiting / 0 Succeeded / 0 Failed
Pod Template:
  Labels:  pod-template-hash=1652693485
           qcloud-app=mq-svc
  Containers:
   queue-mq:
    Image:      rabbitmq:management
    Port:       <none>
    Host Port:  <none>
    Limits:
      cpu:     500m
      memory:  1Gi
    Requests:
      cpu:        250m
      memory:     256Mi
    Environment:  <none>
    Mounts:       <none>
  Volumes:        <none>
Events:
  Type    Reason            Age   From                   Message
  ----    ------            ----  ----                   -------
  Normal  SuccessfulCreate  50m   replicaset-controller  Created pod: mq-svc-5b96bf78d9-r8n8t
  Normal  SuccessfulCreate  49m   replicaset-controller  Created pod: mq-svc-5b96bf78d9-l4zj2
  Normal  SuccessfulCreate  49m   replicaset-controller  Created pod: mq-svc-5b96bf78d9-m8tmv
  Normal  SuccessfulDelete  49m   replicaset-controller  Deleted pod: mq-svc-5b96bf78d9-m8tmv
  Normal  SuccessfulCreate  49m   replicaset-controller  Created pod: mq-svc-5b96bf78d9-r9wkj
  Normal  SuccessfulCreate  49m   replicaset-controller  Created pod: mq-svc-5b96bf78d9-8wzpq
  Normal  SuccessfulCreate  49m   replicaset-controller  Created pod: mq-svc-5b96bf78d9-d8gwc
  Normal  SuccessfulDelete  49m   replicaset-controller  Deleted pod: mq-svc-5b96bf78d9-d8gwc
  Normal  SuccessfulDelete  49m   replicaset-controller  Deleted pod: mq-svc-5b96bf78d9-8wzpq
  Normal  SuccessfulDelete  49m   replicaset-controller  Deleted pod: mq-svc-5b96bf78d9-l4zj2
  Normal  SuccessfulDelete  49m   replicaset-controller  Deleted pod: mq-svc-5b96bf78d9-r9wkj
  Normal  SuccessfulDelete  45m   replicaset-controller  Deleted pod: mq-svc-5b96bf78d9-r8n8t


--- show deploy 

[root@VM_0_17_centos ~]# kubectl describe deploy  mq-svc
Name:                   mq-svc
Namespace:              default
CreationTimestamp:      Fri, 17 Aug 2018 17:21:13 +0800
Labels:                 qcloud-app=mq-svc
Annotations:            deployment.changecourse=Updating
                        deployment.kubernetes.io/revision=2
                        description=Service based on rabbitmq.
Selector:               qcloud-app=mq-svc
Replicas:               1 desired | 1 updated | 1 total | 1 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        10
RollingUpdateStrategy:  0 max unavailable, 1 max surge
Pod Template:
  Labels:  qcloud-app=mq-svc
  Containers:
   queue-mq:
    Image:      rabbitmq:management
    Port:       <none>
    Host Port:  <none>
    Limits:
      cpu:     500m
      memory:  1Gi
    Requests:
      cpu:        250m
      memory:     256Mi
    Environment:  <none>
    Mounts:       <none>
  Volumes:        <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Progressing    True    NewReplicaSetAvailable
  Available      True    MinimumReplicasAvailable
OldReplicaSets:  <none>
NewReplicaSet:   mq-svc-5b96bf78d9 (1/1 replicas created)
Events:
  Type    Reason             Age   From                   Message
  ----    ------             ----  ----                   -------
  Normal  ScalingReplicaSet  58m   deployment-controller  Scaled up replica set mq-svc-5b96bf78d9 to 2
  Normal  ScalingReplicaSet  57m   deployment-controller  Scaled up replica set mq-svc-5b96bf78d9 to 3
  Normal  ScalingReplicaSet  57m   deployment-controller  Scaled up replica set mq-svc-5b96bf78d9 to 4
  Normal  ScalingReplicaSet  57m   deployment-controller  Scaled down replica set mq-svc-5b96bf78d9 to 3
  Normal  ScalingReplicaSet  57m   deployment-controller  Scaled up replica set mq-svc-5b96bf78d9 to 6
  Normal  ScalingReplicaSet  57m   deployment-controller  Scaled down replica set mq-svc-5b96bf78d9 to 4
  Normal  ScalingReplicaSet  56m   deployment-controller  Scaled down replica set mq-svc-5b96bf78d9 to 2
  Normal  ScalingReplicaSet  53m   deployment-controller  Scaled down replica set mq-svc-5b96bf78d9 to 1
```

### deployment和service区别
```
kind: Service 
apiVersion: v1 
metadata:
  name: hostname-service 
spec:
  # Expose the service on a static port on each node
  # so that we can access the service from outside the cluster 
  type: NodePort

  # When the node receives a request on the static port (30163)
  # "select pods with the label 'app' set to 'echo-hostname'"
  # and forward the request to one of them
  selector:
    app: echo-hostname 

  ports:
    # Three types of ports for a service
    # nodePort - a static port assigned on each the node
    # port - port exposed internally in the cluster
    # targetPort - the container port to send requests to
    - nodePort: 30163
      port: 8080 
      targetPort: 80
```

```
解释了spec下面type的集中类型
What does ClusterIP, NodePort, and LoadBalancer mean?
The type property in the Service's spec determines how the service is exposed to the network. It changes where a Service is able to be accessed from. The possible types are ClusterIP, NodePort, and LoadBalancer

ClusterIP – The default value. The service is only accessible from within the Kubernetes cluster – you can’t make requests to your Pods from outside the cluster!

NodePort – This makes the service accessible on a static port on each Node in the cluster. This means that the service can handle requests that originate from outside the cluster.

LoadBalancer – The service becomes accessible externally through a cloud provider's load balancer functionality. GCP, AWS, Azure, and OpenStack offer this functionality. The cloud provider will create a load balancer, which then automatically routes requests to your Kubernetes Service
```

### service 和 ingress的差异

```
可以将ingress理解为七层负载， service下面的pod分发流量为四层负载
internet流量 -> ingress(根据不同域名先分发) -> service
例如有两个域名, 配置如下：

apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: public-services
  namespace: default
spec:
  rules:
  - host: service1.example.com
    http:
      paths:
      - backend:
          serviceName: service1
          servicePort: 80
        path: /
  - host: service2.example.com
    http:
      paths:
      - backend:
          serviceName: service2
          servicePort: 80
        path: /service2

```

