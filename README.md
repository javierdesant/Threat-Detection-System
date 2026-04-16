# Tasks

## Task 1: Sensor nodes and PXE boot
- Develop and set up an infrastructure consisting of one or more sensor nodes with single-board computers (Raspberry Pi 5) and either:
  - a Raspberry Pi AI Camera module, or
  - a Raspberry Pi Camera Module plus a Raspberry Pi AI HAT.
- Deploy the operating system (for example, Raspberry Pi OS or Ubuntu) and the object detection software (for example, YOLO [1], [2] or TensorFlow).
- Investigate how the operating system images of the Raspberry Pi 3 nodes can be consolidated on a Raspberry Pi 4 or Raspberry Pi 5.
- The goal is to boot the Raspberry Pi 3 nodes via PXE over the LAN and simplify the administration of the cluster.
- Try it out and investigate the benefits and drawbacks of such a deployment scenario.

## Task 2: Performance measurement with HPL
- Investigate the performance (GFLOPS) of your infrastructure or cluster system by using the industry standard solution HPL (High Performance LINPACK).

## Task 3: MPI on the cluster
- Deploy the Message Passing Interface (MPI) on the cluster to make it a high-performance cluster.
- The Raspberry Pi 3 nodes can act as worker nodes, while the Raspberry Pi 4 or Raspberry Pi 5 acts as the master node.
- Demonstrate the scalability of the cluster using MPI applications and analyze the potential performance as well as the bottlenecks.
- Also demonstrate Amdahl's Law and Gustafson's Law using at least two MPI examples.

## Task 4: Non-MPI demonstration of scaling laws
- Demonstrate Amdahl's Law and Gustafson's Law by using a non-MPI tool such as Task Distributor.

## Task 5: Monitoring solution
- Deploy a monitoring solution that observes:
  - the health status of the hardware,
  - relevant operating system parameters,
  - service parameters, and
  - network services.
- Use an open source tool such as Prometheus, Grafana, or CheckMK.

## Task 6: Image collection and model training
- Collect a sufficient number of images for the training and testing of your object detection model (for example, TensorFlow, OpenCV, YOLO) using:
  - your own hardware (in this case you need a supported GPU), or
  - a cloud service (for example, Roboflow or V7).
- You are expected to train your own model.
- Using a pre-existing model is not sufficient.

## Task 7: Backend development
- Develop a backend to manage the sensor nodes and the collected data.
- The backend can be deployed as Docker container(s) on a Raspberry Pi Kubernetes cluster with k3s or a similar solution.
- The backend infrastructure will be a robust and scalable high-availability cluster of Raspberry Pi 3 nodes.
- The cluster includes:
  - a distributed file system (for example, Ceph with the Ceph Object Gateway S3 API), or
  - a storage service (for example, SeaweedFS or MinIO).

## Task 8: Frontend development
- Develop a frontend to present, for example:
  - log information,
  - event messages, and
  - a map of events with supporting evidence such as images and timestamps.
- The frontend will also be deployed as a Docker container on a Raspberry Pi Kubernetes cluster with k3s or a similar solution.
- It should be implemented with a modern framework such as Vue.js or React.
- Use protocol(s) such as REST or MQTT for communication between the components (frontend, backend, services, etc.).

## Task 9: Telegram notifications
- Implement a Telegram notification feature with a Telegram Bot.
- The Telegram Bot informs the team members about:
  - health-related events of the infrastructure, and
  - threats or other events detected by the sensor node(s).

## Task 10: Documentation and presentation
- Document and present the results from Tasks 1 to 9.
- Create documentation and guides that enable students, researchers, and lecturers to reproduce the edge computing scenarios and use them for their own modules and research projects.
- No slide presentations or traditional PDF project reports will be created.
- Instead, each team develops complete and understandable online documentation (for example via GitHub Pages) and presents the results in the form of:
  - a poster, and
  - a live demonstration.
