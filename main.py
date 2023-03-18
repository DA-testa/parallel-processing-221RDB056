# python3

def parallel_processing(n, m, data):
    output = []
    threads = []
    for i in range(n):
        threads.append(i)
    
    print(threads)
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
    print(data)
    assert len(data) == m, "Incorrect job count"

    # Calls function which calculates parallel processing
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
