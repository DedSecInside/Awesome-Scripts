#!/usr/bin/env python3
import asyncio, asyncssh

#Can be used for asynchronous remote shut down any number of linux machines in a network with same login credentials.

async def run_client(host, command):
      """
      Run a command on the given host.

      Args:
          host: (str): write your description
          command: (str): write your description
      """
#   async with asyncssh.connect(host, username='username', password='password') as conn:
    async with asyncssh.connect(host, username='username') as conn:
        return await conn.run(command)

async def run_multiple_clients():
      """
      Run multiple hosts.

      Args:
      """
    # Put your lists of hosts here
    hosts = ['192.168.1.100', '192.168.1.101', '192.168.1.102']

    tasks = (run_client(host, "echo 'password' | sudo -S init 0") for host in hosts)
    results = await asyncio.gather(*tasks, return_exceptions=True)
    #print(results)
    for i, result in enumerate(results, 1):
        #you might have to change the if else stuff based on the command you choose to execute
        if isinstance(result, Exception):
            print('Task %d failed: %s' % (i, str(result)))
        elif not result.stdout:
            print('Task %d : Connection closed by remote host.' % (i))

#        print(75*'-')

asyncio.get_event_loop().run_until_complete(run_multiple_clients())