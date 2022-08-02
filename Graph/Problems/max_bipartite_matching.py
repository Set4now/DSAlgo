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
            if self.graph[applicant][job] == 1 and job not in seen:
                seen.add(job)
                
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


        """
        job_applications = [-1] * self.jobs  

        maxmatch  = 0
        for applicant in range(self.applicants):
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