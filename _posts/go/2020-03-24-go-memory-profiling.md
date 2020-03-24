---
title: Memory analysis in Go
date: 2019-03-24 11:11:00 +0530
categories: [Go, Guidelines]
tags: [go, golang, guidelines, profiling]
summary: Generic references and points to consider when doing a memory analysis with go programming language.
---

Generic references and points to consider when doing a memory analysis with go programming language.

- Do [pprof memory profiling](https://github.com/golang/go/wiki/Performance#memory-profiler).

- Go returns memory to OS gradually. Typical time is ~5 minutes. If immediate return is needed, we could use [FreeOSMemory](https://golang.org/pkg/runtime/debug/#FreeOSMemory). General recommendation is that if this is needed, manage memory alternatively.

- Alternative for frequent allocated and reused objects is sync.Pool usage. This is tricky and have to be careful when doing this. Sample usage can be found in [blog](https://www.akshaydeo.com/blog/2017/12/23/How-did-I-improve-latency-by-700-percent-using-syncPool/).

- Excellant High performance go tips are avilable at this [post](https://dave.cheney.net/high-performance-go-workshop/dotgo-paris.html#memory-and-gc). This talks about memory and GC too.

- Garbage collection behaviour is well explianed at: Ardan labs [Post 1](https://www.ardanlabs.com/blog/2018/12/garbage-collection-in-go-part1-semantics.html), [Post 2](https://www.ardanlabs.com/blog/2019/05/garbage-collection-in-go-part2-gctraces.html) and [Post 3](https://www.ardanlabs.com/blog/2019/07/garbage-collection-in-go-part3-gcpacing.html). Also there is this [keynote](https://blog.golang.org/ismmkeynote) explaining the evolution of Go's garbage collector.
