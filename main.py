# python3

def parallel_processing(n, m, data):
    output = []
    threads = []
    current_job = 0
    second = 0
    for i in range(n):
        threads.append((i,0))
    for x in range(m):
        for i in range(n):
            if threads[i][1] == 0:
                threads[i] = (threads[i][0], data[x])
                output.append((threads[i][0], second))
                current_job += 1
        second += 1
    return output

def main():
    # n - contains thread count
    # m - contains job count
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
    
    for job in result:
        print(job[0], job[1])

if __name__ == "__main__":
    main()
