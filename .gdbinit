set architecture riscv:rv64

target remote localhost:1234

hbreak *0x8e2e4000

layout regs
display /i $pc

define sc
    set $next_insn = $pc + 4
    thbreak *$next_insn
    continue
end
document sc
    Sets a temporary hardware breakpoint at $pc + 4 and continues.
end

continue
