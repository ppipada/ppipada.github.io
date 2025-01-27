# Sorting

## Complexity summary

| Algorithm                                                     | Best          | Average          | Worst            | Space Complexity |
| ------------------------------------------------------------- | ------------- | ---------------- | ---------------- | ---------------- |
| [Quicksort](http://en.wikipedia.org/wiki/Quicksort)           | `Ω(n log(n))` | `Θ(n log(n))`    | `O(n^2)`         | `O(log(n))`      |
| [Mergesort](http://en.wikipedia.org/wiki/Merge_sort)          | `Ω(n log(n))` | `Θ(n log(n))`    | `O(n log(n))`    | `O(n)`           |
| [Timsort](http://en.wikipedia.org/wiki/Timsort)               | `Ω(n)`        | `Θ(n log(n))`    | `O(n log(n))`    | `O(n)`           |
| [Heapsort](http://en.wikipedia.org/wiki/Heapsort)             | `Ω(n log(n))` | `Θ(n log(n))`    | `O(n log(n))`    | `O(1)`           |
| [Bubble Sort](http://en.wikipedia.org/wiki/Bubble_sort)       | `Ω(n)`        | `Θ(n^2)`         | `O(n^2)`         | `O(1)`           |
| [Insertion Sort](http://en.wikipedia.org/wiki/Insertion_sort) | `Ω(n)`        | `Θ(n^2)`         | `O(n^2)`         | `O(1)`           |
| [Selection Sort](http://en.wikipedia.org/wiki/Selection_sort) | `Ω(n^2)`      | `Θ(n^2)`         | `O(n^2)`         | `O(1)`           |
| [Tree Sort](https://en.wikipedia.org/wiki/Tree_sort)          | `Ω(n log(n))` | `Θ(n log(n))`    | `O(n^2)`         | `O(n)`           |
| [Shell Sort](http://en.wikipedia.org/wiki/Shellsort)          | `Ω(n log(n))` | `Θ(n(log(n))^2)` | `O(n(log(n))^2)` | `O(1)`           |
| [Bucket Sort](http://en.wikipedia.org/wiki/Bucket_sort)       | `Ω(n+k)`      | `Θ(n+k)`         | `O(n^2)`         | `O(n)`           |
| [Radix Sort](http://en.wikipedia.org/wiki/Radix_sort)         | `Ω(nk)`       | `Θ(nk)`          | `O(nk)`          | `O(n+k)`         |
| [Counting Sort](https://en.wikipedia.org/wiki/Counting_sort)  | `Ω(n+k)`      | `Θ(n+k)`         | `O(n+k)`         | `O(k)`           |
| [Cubesort](https://en.wikipedia.org/wiki/Cubesort)            | `Ω(n)`        | `Θ(n log(n))`    | `O(n log (n))`   | `O(n)`           |

## Quicksort

- Quicksort is a divide-and-conquer algorithm.
- It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.
- The sub-arrays are then sorted recursively.
- This can be done in-place, requiring small additional amounts of memory to perform the sorting.
- Stable: `No`

![Alt text](../images/quicksort.gif?raw=true "Quicksort")

## Mergesort

- _Mergesort_ is also a divide and conquer algorithm. It continuously divides an array into two halves, recurses on both the left subarray and right subarray and then merges the two sorted halves
- Stable: `Yes`

![Alt text](../images/mergesort.gif?raw=true "Mergesort")

## Bucket Sort

- _Bucket Sort_ is a sorting algorithm that works by distributing the elements of an array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the bucket sorting algorithm

![Alt text](../images/bucketsort.png?raw=true "Bucket Sort")

## Radix Sort

- _Radix Sort_ is a sorting algorithm that like bucket sort, distributes elements of an array into a number of buckets. However, radix sort differs from bucket sort by 're-bucketing' the array after the initial pass as opposed to sorting each bucket and merging
