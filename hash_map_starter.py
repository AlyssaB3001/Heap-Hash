# hash_map_starter.py
# Tiny educational HashMap using separate chaining.
# Goal: implement put/get/remove with a fixed-size bucket array.
# NOTE: Keep it simple; resizing is not required for this lab.

from typing import Any, List, Tuple, Optional

class HashMap:
    def __init__(self, capacity: int = 8):
        # Each bucket is a list of (key, value) pairs
        self._buckets: List[List[Tuple[Any, Any]]] = [[] for _ in range(capacity)]
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def _index(self, key: Any) -> int:
        # Map a key to bucket index
        return hash(key) % len(self._buckets)

    def put(self, key: Any, value: Any) -> None:
        """Insert or update (key, value)."""
        i = self._index(key)
        bucket = self._buckets[i]
        #TODO: If key exists in bucket, update its value. Else append and increase _size.
         #Add code here – remove pass
        pass

    def get(self, key: Any) -> Optional[Any]:
        """Return value for key or None if not found."""
        i = self._index(key)
        bucket = self._buckets[i]
        #TODO: Scan bucket; if key found, return value. Otherwise, return None.
        #Add code here – remove the pass
        pass

    def remove(self, key: Any) -> bool:
        """Remove key if present; return True if removed else False."""
        i = self._index(key)
        bucket = self._buckets[i]
        #TODO: Find key, pop it from bucket, decrease _size, return True; else False.
        #Add code here – remove the pass
        pass


if __name__ == "__main__":
    #demo (prints only)
    m = HashMap(capacity=4)
    m.put("alice", 10)
    m.put("bob", 20)
    m.put("alice", 11)  # update
    print("size:", len(m))       # expect 2
    print("alice:", m.get("alice"))  # expect 11
    print("bob:", m.get("bob"))      # expect 20
    print("missing:", m.get("zzz"))  # expect None
    print("removed bob:", m.remove("bob"))  # expect True
    print("size now:", len(m))       # expect 1
