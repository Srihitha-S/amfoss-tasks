Terminal Voyage - Task 01 Solution Narrative

Level 1: Loguetown Reef

The challenge began by cloning the main GitHub repository onto the local machine and navigating directly into the project root directory. From there, I switched the repository state to the timeline branch and moved into the GrandLine/Loguetown_Reef working directory.

To determine how the script functioned, I opened and read the contents of eat.sh. The script was designed to check for executable permissions on devil fruit text files passed to it. Listing the directory contents showed that sector_C/devil_fruit_6.txt was colored green, indicating active executable permissions. Executing ./eat.sh with sector_C/devil_fruit_6.txt as its input argument outputted the first flag: ONE_PIECE{GITO_GITO_NO_AWAKENING}.
Level 2: Whiskey Peak

Moving back into the GrandLine parent folder, I entered the Whiskey_Peak directory and inspected all files, including reading feast_manifest.txt. Running a full branch check with git branch -a exposed a remote tracking branch named remotes/origin/whiskey_peak_investigation.

After checking out this branch, re-inspecting the folder contents brought up a newly visible text report named intercepted_report.txt as well as a hidden folder named .baroque_works_cache. Entering this hidden cache directory, I exported the Level 1 flag as an environment variable named AWAKENING_SIGNATURE, ran the unlock_vault.sh script, and compared the output logs (marine_intercept.log and bounty_hunter_feed.log) using diff. The difference between the two logs revealed the level flag: BAROQUE_DIAL{SPLIT_TIMELINE_MISDIRECTION}.
Level 3: Little Garden

Returning to the GrandLine directory once again, I checked out the little_garden branch and navigated into the Little_Garden folder, followed by Wax_Jungle. There, I converted the Level 2 flag string into its corresponding MD5 hash.

Using a recursive string search across the subfolders, I located references leading to an agent manifest log file located deep inside the sector_beta/outpost/watchtower/storage/archive directory. Opening agent_manifest.log provided the first Poneglyph fragment: PONEGLYPH_FRAGMENT_I = "KjY2MjF4bW0lKzYqNyBsIS0vbTAtJTcnL".
Level 4: Water 7

I stepped back out into the root directory and navigated into Water_7, where I found a compressed blueprint archive. I unpacked the primary tarball puffing_tom_blueprints, which extracted a nested archive titled step1_blueprints.zip.

Unzipping this second archive generated a blueprints_extracted folder. Reading the secret_link.txt file inside revealed the second Poneglyph fragment: PONEGLYPH_FRAGMENT_II = "SwnbzptDiM3JspvFiMuJ28PJzAlJ28VIzA=".
Level 5: Enies Lobby

I moved back to the GrandLine directory and listed all repository branches to find the target alternate history. Switching over to the alternate_timeline branch, I inspected the recent commit history using git log to find the last intact commit before destruction occurred (d4e7bf5), and checked out that specific commit hash.

Inside the Enies_Lobby folder, I ran a short Python script to concatenate the two base64 fragments from Level 3 and Level 4 and perform an XOR decryption using the hexadecimal key 0x42. Decoding the resulting raw bytes yielded the URL for the final repository: [https://github.com/rogueone-x/Laugh-Tale-Merge-War.git](https://github.com/rogueone-x/Laugh-Tale-Merge-War.git).
Level 6: Laugh Tale (Merge War)

To complete the final stage, I cloned the newly discovered repository and entered its project folder. I attempted to merge the origin/pirate_king_path branch into the current working branch, which triggered intentional git merge conflicts inside treasure/key_part_1.txt and treasure/key_part_2.txt.

Opening both text files, I manually cleared the conflict markers to reconstruct the full passphrase, which assembled into TheGrandLineRemembers. After staging the resolved files and committing the merge resolution, I executed the ./victory.sh script. When prompted, I submitted the passphrase, which generated the final challenge flag: FLAG{The_Grand_Line_Remembers_Your_Commit}.
