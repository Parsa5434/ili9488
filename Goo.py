import multiprocessing
import os

def write_range(start, end, filename, buffer_size=10_000_000):
    buffer = []
    written = 0
    with open(filename, "w") as f:
        for i in range(start, end):
            buffer.append(f"{i}\n")
            if len(buffer) >= buffer_size:
                f.write("".join(buffer))
                written += len(buffer)
                buffer.clear()
        if buffer:
            f.write("".join(buffer))
            written += len(buffer)
    print(f"[{filename}] Done writing {written} numbers.")

if __name__ == "__main__":
    start = 9999999
    end = 1000000000
    num_processes = multiprocessing.cpu_count()

    total_numbers = end - start
    chunk_size = total_numbers // num_processes

    processes = []
    for i in range(num_processes):
        chunk_start = start + i * chunk_size
        chunk_end = chunk_start + chunk_size if i < num_processes - 1 else end
        filename = f"numbers_part_{i}.txt"
        p = multiprocessing.Process(target=write_range, args=(chunk_start, chunk_end, filename))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("✅ All parts written in parallel.")
  
