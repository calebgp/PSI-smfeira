import queue

q = queue.LifoQueue()
q.put("Caleb")
q.put("João")
q.put("Paulo")
while not q.empty():
  e = q.get()
  print(e)
