"""

EC2 Recommendation
Python script that provides EC2 instance recommendations based on a given instance's type, size, and CPU utilization. The script will help in recommending appropriate EC2 instances for optimizing performance and costs based on the utilization metrics.
Input:
Current EC2 Instance: A string representing the instance type and size (e.g., t2.nano, t3.medium).
CPU Utilization: A percentage value representing the current CPU utilization (e.g., 40%).

The output will be a recommendation for a new EC2 instance based on the following logic:

Underutilized: If the CPU utilization is less than 20%, recommend a smaller instance.
Optimized: If the CPU utilization is between 20% and 80%, recommend the same instance size but suggest the latest generation instance type.
Overutilized: If the CPU utilization is greater than 80%, recommend a larger instance.
 
Instance Size Comparison: The EC2 instance sizes follow a specific hierarchy:

nano > micro > small > medium > large > xlarge > 2xlarge > 4xlarge > 8xlarge > 16xlarge > 32xlarge..

If the CPU is underutilized (CPU < 20%), the script should recommend a smaller instance by one step.
If the CPU is overutilized (CPU > 80%), the script should recommend a larger instance by one step.
If the instance size is the smallest (nano), it cannot be reduced further, so no smaller size is recommended.
If the instance is the largest (32xlarge), it cannot be upgraded further.

Input 1: 
Current EC2 : t2.large
CPU : 20%

Output 1:
Table showing columns and its value (use Que 6 function to make table with following columns)
Columns are : serial no., current ec2, current CPU, status, recommended ec2
"""




import pandas as pd

instanceTypes = ['nano', 'micro', 'small', 'medium', 'large', 'xlarge', '2xlarge', '4xlarge', '8xlarge', '16xlarge', '32xlarge']

def recommendedInstance(currEc2, currCPU):
    instance_type, instance_size = currEc2.split('.')

    currIdx = instanceTypes.index(instance_size)

    if currCPU < 20:
        
        if currIdx > 0:
            recommended = instanceTypes[currIdx - 1]
        else:
            recommended = instance_size  
        status = 'Underutilized'
    elif 20 <= currCPU <= 80:
        recommended = instance_size  
        status = 'Optimized'
    else:
        if currIdx < len(instanceTypes) - 1:
            recommended = instanceTypes[currIdx + 1]
        else:
            recommended = instance_size  
        status = 'Overutilized'
    
    recommended_ec2 = f"{instance_type}.{recommended}"
    return currEc2, currCPU, status, recommended_ec2

def genereateTable(currEc2, currCPU):
    recommendations = []
    recommendations.append(recommendedInstance(currEc2, currCPU))
    
    df = pd.DataFrame(recommendations, columns=['Current EC2', 'Current CPU (%)', 'Status', 'Recommended EC2'])
    df.index += 1 
    df.insert(0, 'Serial No.', df.index)  
    return df


currEc2 = input("Enter the current EC2 instance (e.g., t2.large): ")
currCPU = float(input("Enter the current CPU utilization (e.g., 20.5): "))

df = genereateTable(currEc2, currCPU)

print(df)