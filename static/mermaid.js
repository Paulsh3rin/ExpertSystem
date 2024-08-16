graph TD
    A[User Submits Form] --> B[Flask Server Receives Request]
    B --> C[Expert System Processes Symptoms]
    C --> D{Inference Engine}
    D --> |Yes| E[Return Diagnosis and Medications]
    D --> |No| F[Return 'No Diagnosis Found']
    E --> G[Display Result to User]
    F --> G[Display Result to User]
