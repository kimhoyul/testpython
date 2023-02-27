import asyncio
import time

from main_functions import main

start_time = time.time()
asyncio.run(main())
end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed Time:", elapsed_time, "seconds")
