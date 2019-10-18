class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # check if the capacity is full
    # if the capacity is not full add to tail
    # if the capacity is full remove from head
    # then add to head.
    if self.current == self.capacity:
      self.current = 0
    self.storage[self.current] = item
    self.current +=1

  def get(self):
    return list(filter(None ,self.storage))
   