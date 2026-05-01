# test_counter.py
import random
import cocotb
from cocotb.clock    import Clock
from cocotb.triggers import RisingEdge
from cocotb.triggers import Timer

async def start_clock(dut):
    """クロック生成"""
    clock = Clock(dut.clk, 10, units="ns")  # 10ns周期のクロック
    cocotb.start_soon(clock.start())

async def reset_dut(dut):
    """リセット処理"""
    dut.rst_n.value = 0  # アクティブローのリセット
    await RisingEdge(dut.clk)  # クロックの立ち上がりを待つ
    dut.rst_n.value = 1  # リセット解除

@cocotb.test()
async def test_counter_basic(dut):
    await start_clock(dut)  # クロック生成
    await reset_dut(dut)    # リセット処理

    # クロック生成（10ns周期）
#    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # リセット
#    dut.rst_n.value = 0
#    await RisingEdge(dut.clk)
#    dut.rst_n.value = 1

    dut.en.value = 1  # カウンタ有効
    # カウント確認
    for i in range(2**8-1):  # 255までカウント
        await RisingEdge(dut.clk)
        await Timer(1, units='ns')
        assert int(dut.count.value) == i + 1, f"FAILED: Expected to be {i+1}, but got {dut.count.value}"

@cocotb.test()
async def test_counter_random(dut):
    await start_clock(dut)  # クロック生成
    await reset_dut(dut)    # リセット処理

    # クロック
#    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # リセット
#    dut.rst_n.value = 0
#    dut.en.value = 0
#    await RisingEdge(dut.clk)
#    dut.rst_n.value = 1

    expected = 0

    for cycle in range(2**8-1):  # 255までカウント

        # ランダム入力
        en = random.randint(0, 1)
        dut.en.value = en

        await RisingEdge(dut.clk)
        await Timer(1, units='ns')

        # Goldenモデル更新
        if en:
            expected += 1

        # チェック
        actual = int(dut.count.value)
        assert actual == expected, f"Mismatch at cycle {cycle}: expected={expected}, actual={actual}"