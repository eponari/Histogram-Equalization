class picture:
  def __init__(self):
    #create a list for our matrix
    self.matrix=[]
  def get_matrix(self):
    #get the number of rows and colomns
    print("Enter the numbe of rows and columns seperated by space:")
    self.rows,self.colomns=[int(x) for x in input().split()]
    #get each row one by one
    print("Enter each row:")
    for i in range(self.rows):
      row=[int(x) for x in input().split()]
      self.matrix.append(row)
  def histogram_equalization(self):
    #keep track of the frequency of each number and the range of elements
    frequency={}
    max_element=self.matrix[0][0]
    #iterate each element and look for the frequency and the range
    for row in self.matrix:
      for element in row:
        max_element=max(max_element,element)
        if element in frequency:
          frequency[element]+=1
        else:
          frequency[element]=1

    #intensity range is always in the form of 2^n-1
    intensity_range=1
    while(intensity_range<max_element):
      intensity_range*=2
    max_element=intensity_range-1

    #sort the dictionary according to its keys
    frequency=sorted(frequency.items(),key=lambda x: x[0])

    #create a new dictionary to keep track of the new frequencies we see
    new_frequency={}
    #This is used in the summation proccess
    previous_value=0

    for number,freq in frequency:
      #we see the probability of each m*n elements by its frequency
      probability_of_element=freq/(self.rows*self.colomns)
      
      #the new value is the previous one plus the intensity range times the probability of this element
      new_value=previous_value+(probability_of_element*max_element)
      
      #the previous value takes the value of the new variable and we round the new value to put it in our dictionary
      previous_value=new_value
      new_value=round(new_value)

      if new_value in new_frequency:
        new_frequency[new_value]+=freq
      else:
        new_frequency[new_value]=freq

    #iterate through the new dictionary and print the new value and frequency realtion
    print("The new distribution of intensities in increasing order is:")
    for number,freq in new_frequency.items():
      print(number,freq)