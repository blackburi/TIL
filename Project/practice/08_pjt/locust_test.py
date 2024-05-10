from locust import HttpUser, task, between

class SampleUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        print('test start')

    # @task
    # def normal_sort(self):
    #     self.client.get("test/normal_sort/")
    
    # @task
    # def csv_to_df(self):
    #     self.client.get("test/csv_to_df/")

    # @task
    # def dropna(self):
    #     self.client.get("test/dropna/")
        
    @task
    def age_nearest(self):
        self.client.get("test/age_nearest/")
    @task
    def average_test(self):
        self.client.get("test/average_test/")

    # @task
    # def priority_queue(self):
    #     self.client.get("test/priority_queue/")

    # @task
    # def bubble_sort(self):
    #     self.client.get("test/bubble_sort/")


