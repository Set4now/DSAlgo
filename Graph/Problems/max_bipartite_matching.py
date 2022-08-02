"""
Maximum Bipartite Matching

There are M job applicants and N jobs.  
Each applicant has a subset of jobs that he/she is interseted in. 
Each job opening can only accept one applicant and a job applicant can be appointed for only one job. 
Given a matrix G where G(i,j) denotes ith applicant is interested in jth job.
Find an assignment of jobs to applicant in such that as many applicants as possible get jobs.


Algorithm

bpm() Create a DFS function 
    for all the jobs the applicant is intertested in and job which is not seen yet
        mark the job as seen or visited
        if the job is not assigned to anyone, 
            assign to the applicant and return True
        else
            whoever the job is already assigned to eg. (X), rescusrively call the DFS function for X to see if any other
            job can be assigned to it and return True

call the bpm() for all the applicants and keep incrementing count as long as bpm returns true



Detailed explanation

1.
    Maintain an assign[] array to keep track of which job is assigned to which applicant. 
    For instance, assign[1]=2 means job number 1 is assigned to applicant number 2.
2.   
    Each applicant will maintain a visited[] array to keep track of which jobs the candidate was already considered (to avoid going in loops).

3.
    For each applicant do the Depth-First Search (DFS) (to find a job). 
        Iterate through all the jobs and for each job
        check if applicant can do this job and applicant was never considered for this job (adjMatrix[applicant][job] == 1 && visited[job]==false), if yes then mark visited[job]==true (applicant is being considered for this job now and will not be considered again)
        check if the job is not assigned to any other applicant (assign[job]==-1) – then assign the job to this applicant OR If the job was assigned earlier to any other applicant say ‘X’ earlier then make the recursive call for applicant ‘X’ (do another DFS) to check if some other job can be assigned applicant ‘X’ If that happens, assign this job to the current applicant and break the current loop 3a and check for the next applicant. and If this job cannot be assigned to this applicant then check for the next job.


"""


class Solution:
    def maximumMatch(self, G):
        self.graph = G
        self.applicants = len(G)
        self.jobs = len(G[0])
        return self.maxmatch()

    def bpm(self, applicant, seen, job_applications):
        for job in range(self.jobs):
            # 1 Means the applicant is interested in that job
            # check if applicant can do this job and applicant was never considered for this job
            if self.graph[applicant][job] == 1 and job not in seen:
                seen.add(job) # applicant is being considered for this job now and will not be considered again
                
                """
                the job (A) is not assigned to anyone or
                if the job (A) is already assigned to someone (X), can we allocate another job (B) to (X)
                and assign the current Job (A) to the current applicant.
                
                """
                if job_applications[job] == -1 or self.bpm(job_applications[job], seen, job_applications):
                    job_applications[job] = applicant
                    return True

        return False
    

    def maxmatch(self):
        """
        an array to keep track of all the job to applicant 1:1 mapping 
        Applicants are numbered from 0 - (N - 1)
        Jobs are numbered from 0 - (M - 1)

        job_applications[job] = applicant

        """
        job_applications = [-1] * self.jobs  

        maxmatch  = 0
        for applicant in range(self.applicants):
            # Each applicant will maintain a seen set to keep track of which jobs the candidate was already considered (to avoid going in loops).
            seen = set()
            if self.bpm(applicant, seen, job_applications):
                maxmatch += 1
        return maxmatch

bpGraph =[[0, 1, 1, 0, 0, 0],
          [1, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0],
          [0, 0, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1]]
 
s = Solution()
print(s.maximumMatch(bpGraph))