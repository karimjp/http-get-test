import time
import unirest

class GetRequestTest:
  responses = []
  start_time = None

  def __init__(self, number_of_requests):
      self.number_of_requests = number_of_requests

  @staticmethod
  def callback_function(response):
      print response.code
      end_time = time.time() 
      completion_time = end_time - GetRequestTest.start_time
      GetRequestTest.responses.append(completion_time)
  
  def run(self):
      unirest.timeout(100)
      GetRequestTest.start_time = time.time()
      for i in range(self.number_of_requests):
          url = "http://0.0.0.0:5000/predict"
          body = "test" + str(i)
          print "Request: ", url, body 
          unirest.get(url, params={ "text": body}, callback=GetRequestTest.callback_function)

if __name__ == '__main__':
    number_of_requests = 4
    GRT = GetRequestTest(number_of_requests)
    GRT.run()
    while len(GRT.responses) < number_of_requests:
        pass #stalling
    print GRT.responses
