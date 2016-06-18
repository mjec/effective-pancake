#!/usr/bin/env python3

print("""

{heading_col_start}  _____                _  _     _                      _    {end}
{heading_col_start} |  __ \              ( )| |   | |                    | |   {end}
{heading_col_start} | |  | |  ___   _ __ |/ | |_  | |_  _ __  _   _  ___ | |_  {end}
{heading_col_start} | |  | | / _ \ | '_ \   | __| | __|| '__|| | | |/ __|| __| {end}
{heading_col_start} | |__| || (_) || | | |  | |_  | |_ | |   | |_| |\__ \| |_  {end}
{heading_col_start} |_____/  \___/ |_| |_|   \__|  \__||_|    \__,_||___/ \__| {end}
{heading_col_start}                _   _ __     __ ____   _   _  ______        {end}
{heading_col_start}         /\    | \ | |\ \   / // __ \ | \ | ||  ____|       {end}
{heading_col_start}        /  \   |  \| | \ \_/ /| |  | ||  \| || |__          {end}
{heading_col_start}       / /\ \  | . ` |  \   / | |  | || . ` ||  __|         {end}
{heading_col_start}      / ____ \ | |\  |   | |  | |__| || |\  || |____        {end}
{heading_col_start}     /_/    \_\|_| \_|   |_|   \____/ |_| \_||______|       {end}
{heading_col_start}                                                            {end}

     ________________________________________ 
    / Lesson one: Don't trust anyone! {red}You{end}    \ 
    | {red}have just let me run arbitrary code on{end} | 
    \ {red}your computer.{end} This is dangerous.      / 
     ---------------------------------------- 
            \   ^__^
             \  (@@)\_______
                (__)\       )\/\ 
                    ||----w |
                    ||     ||

When you run vagrant up, whatever scripts the author has put in the Vagrantfile
will run with your permissions. This lets me run arbitrary code on your
computer!

{red}Edit the Vagrantfile in this directory{end} and:

 * comment out line {offending_line}, which reads:

    config.vm.synced_folder "/etc", "/host_etc", disabled: true

   by adding a leading #.

   That line lets me read your /etc directory. I could then use this script
   to send your secret data to a server I control. Wouldn't that suck for you?
   Thankfully it is disabled, but that's only because I'm nice.

   Don't think that's scary? I could also read your ~/.ssh/id_rsa file and then
   I would have your SSH keys. Do you store AWS keys anywhere that you can read?
   How about email passwords? How about your cookies and any passwords saved by
   your web browser? I can read all of this. But I haven't, because I'm not evil.

   The lesson here is: don't just run vagrant up.

 * delete lines {insecure_provision_start} to {insecure_provision_end} to stop this warning from appearing in future.

 * check that it isn't doing anything else you don't want it to do. I'm telling
   you that you only need to do those two things, but do you still trust me?

{heading_col_start}                                                            {end}
{heading_col_start}   READ THE MESSAGES ABOVE. SERIOUSLY. THEY'RE IMPORTANT.   {end}
{heading_col_start}                                                            {end}
""".format(
    offending_line=35,
    insecure_provision_start=45,
    insecure_provision_end=52,
    heading_col_start='\x1b[31;43m',
    red='\x1b[31;11m',
    end='\x1b[0m'
))

