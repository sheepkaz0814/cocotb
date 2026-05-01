TOPLEVEL_LANG = verilog
VERILOG_SOURCES = $(PWD)/counter.v
TOPLEVEL = counter
MODULE = test_counter

SIM = verilator
WAVES = 1

.PHONY: basic random all

basic:
	$(MAKE) sim TESTCASE=test_counter_basic
random:
	$(MAKE) sim TESTCASE=test_counter_random
all:
	$(MAKE) sim

include $(shell cocotb-config --makefiles)/Makefile.sim
