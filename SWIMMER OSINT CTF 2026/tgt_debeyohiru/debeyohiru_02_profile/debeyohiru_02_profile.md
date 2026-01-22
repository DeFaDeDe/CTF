# debeyohiru_02_profile

- Description
    
    As of January 2026, `debeyohiru` appears to have been job hunting and had a profile page published online.
    
    Find this page and answer its URL.
    
    For example, if the relevant page were `https://example.com/foobar`, the flag would be `SWIMMER{https://example.com/foobar}`.
    

Knowing the username `furaigo5` in the last challenge, we can find the [link](https://furaigo5.github.io/profile/) very easily

![image.png](images/image.png)

We can also use Sherlock to find the answer; however, there are way too many distractions

```bash
└─$ sherlock furaigo5
.
.
.                                                                                                                                                                                                                    
[*] Checking username furaigo5 on:

[+] 1337x: https://www.1337x.to/user/furaigo5/
[+] Archive.org: https://archive.org/details/@furaigo5
[+] Envato Forum: https://forums.envato.com/u/furaigo5
[+] GNOME VCS: https://gitlab.gnome.org/furaigo5
[+] GeeksforGeeks: https://auth.geeksforgeeks.org/user/furaigo5
[+] GitHub: https://www.github.com/furaigo5
[+] HackenProof (Hackers): https://hackenproof.com/hackers/furaigo5
[+] Hubski: https://hubski.com/user/furaigo5
[+] Letterboxd: https://letterboxd.com/furaigo5
[+] LibraryThing: https://www.librarything.com/profile/furaigo5
[+] NationStates Nation: https://nationstates.net/nation=furaigo5
[+] NationStates Region: https://nationstates.net/region=furaigo5
[+] Slashdot: https://slashdot.org/~furaigo5
[+] Splice: https://splice.com/furaigo5
[+] Spotify: https://open.spotify.com/user/furaigo5
[+] TikTok: https://www.tiktok.com/@furaigo5
[+] Trovo: https://trovo.live/s/furaigo5/
[+] Weblate: https://hosted.weblate.org/user/furaigo5/
[+] YandexMusic: https://music.yandex/users/furaigo5/playlists
[+] mercadolivre: https://www.mercadolivre.com.br/perfil/furaigo5
[+] note: https://note.com/furaigo5
[+] phpRU: https://php.ru/forum/members/?username=furaigo5
[+] svidbook: https://www.svidbook.ru/user/furaigo5

[*] Search completed with 23 results
```

We can still find the [GitHub account](https://github.com/furaigo5): `[+] GitHub: https://www.github.com/furaigo5`, and we can find the profile page after that.

![image.png](images/image%201.png)

Flag: `SWIMMER{https://furaigo5.github.io/profile/}`
