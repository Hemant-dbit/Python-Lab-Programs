import threading
import time
from datetime import datetime

class ATM:
    def __init__(self):
        self.lock = threading.Lock()

    def access_atm(self, user):
        print(f"{user} is waiting to access the ATM at {datetime.now().strftime('%H:%M:%S')}...")
        with self.lock:
            print(f"{user} is accessing the ATM at {datetime.now().strftime('%H:%M:%S')}")
            time.sleep(2)  # Simulate time taken for a transaction
            print(f"{user} has completed the transaction at {datetime.now().strftime('%H:%M:%S')}\n")

atm = ATM()

# Simulate multiple users trying to access the ATM
users = ['Alice', 'Bob', 'Charlie', 'David']
threads = []

start_time = time.time()

for user in users:
    t = threading.Thread(target=atm.access_atm, args=(user,))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

end_time = time.time()
print(f"All transactions completed in {round(end_time - start_time, 2)} seconds.")
