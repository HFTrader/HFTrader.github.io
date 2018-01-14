---
layout: post
title: Cache mistake using HLS with Zynq
category: Xilinx
excerpt: It is a common mistake forgetting about cache when interfacing Zynq and HLS IP
---

It is a very common mistake not to take in account the CPU cache. <br>

You have to issue a Xil_DCacheFlushRange(addr,size) after every write to DDR and Xil_DCacheInvalidateRange(addr,size) before every read to DDR otherwise you will read/write stale values. <br>

See page 5 on <a href="https://www.xilinx.com/support/documentation/sw_manuals/xilinx2015_2/oslib_rm.pdf">UG647</a> <br>
