# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    # n - contains thread count
    # m - contains job count
    thread_job_count = input().split()
    n = int(thread_job_count[0])
    m = int(thread_job_count[1])

    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = input().split()
    assert len(data) == m, "Incorrect job count"

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
