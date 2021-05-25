# Print statements outside of body for cleanlyness
def check_input(train_set, initial_weights, threshold, adjustment_factor):
  for train in train_set:
    if len(train[1]) != len(initial_weights):
      print("Error: Weight length is not equal to number of predictor variables.")
      return 0
    else:
      print("Starting weights: ", initial_weights)
      print("Threshold: ", threshold, "       Adjustment: ", adjustment_factor)
      return 1

def print_pass(i):
  print("")
  print("Pass ", i+1)
  print("")

def print_outcome(training_data, guess, current_weights):
  print("inputs: ", training_data[1])
  print("prediction: ", guess, "       answer: ", training_data[0])
  print("adjusted weights: ", current_weights)

def perceptron(threshold, adjustment_factor, initial_weights, train_set, num_passes):
  if check_input(train_set, initial_weights, threshold, adjustment_factor) == 0:
    return 
  current_weights = initial_weights
  # run the function num_passes times
  for i in range(num_passes):
    print_pass(i)
    # for each training data, make a guess based on the current weights
    for training_data in train_set:
      prediction = 0
      for i in range(len(current_weights)):
        prediction = prediction + (current_weights[i]*training_data[1][i])
      # update prediction based on threshold
      guess = False
      if prediction > threshold:
        guess = True
      # If guess not equal to training y value, update weights based on adjustment factor
      if guess != training_data[0]:
        # if you want it to be more likely to predict, increase the weights
        if (training_data[0] == True) and (guess == False):
          # increase weights by adjustment factor where input is 1
          for j in range(len(current_weights)):
            if training_data[1][j] == 1:
              current_weights[j] += adjustment_factor
        else:
          # decrease weights by adjustment factor where input is 1
          for j in range(len(current_weights)):
            if training_data[1][j] == 1:
              current_weights[j] -= adjustment_factor
      print_outcome(training_data, guess, current_weights)