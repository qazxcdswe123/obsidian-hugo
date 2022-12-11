# Queue

# Priority Queue

```cpp
template<
    class T,
    class Container = std::vector<T>,
    class Compare = std::less<typename Container::value_type>
> class priority_queue;
```

## Example
`std::priority_queue<flightPair, std::vector<flightPair>, std::greater<>> pq;
`
## Links
- [[Queue]]