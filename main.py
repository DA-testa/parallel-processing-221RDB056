# python3

def parallel_processing(n, m, data):
    output = []
    threads = []
    current_job = 0
    second = 0
    end_of_jobs = False

    # Creates a multidimensional list 
    # with two parameteres[thread number, 0 - indicating thread is empty]
    for i in range(n):
        threads.append((i,0))

    # Loops until the last job
    while True:
        # Loops through threads
        for i in range(n):
            # If thread is empty, assigns a job
            if threads[i][1] == 0:
                threads[i] = (threads[i][0], data[current_job])
                output.append((threads[i][0], second))
                current_job += 1
            # If thread is working, updates the time left
            if threads[i][1] > 0:
                threads[i] = (threads[i][0], threads[i][1]-1)
            # If last job reached break out the while loop with a boolean
            if current_job == m:
                end_of_jobs = True
                break
        second += 1
        if end_of_jobs:
            break

    return output

def main():
    # n - thread count
    # m - job count
    thread_job_count = input().split()
    n = int(thread_job_count[0])
    m = int(thread_job_count[1])

    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []
    jobs = input().split()
    for i in range(m): 
        data.append(int(jobs[i]))
    assert len(data) == m, "Incorrect job count"

    # Calls function which calculates parallel processing
    result = parallel_processing(n,m,data)
    
    # Prints the result 
    for job in result:
        print(job[0], job[1])

if __name__ == "__main__":
    main()
