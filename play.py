B
    ²cD];  γ               @   sά   d dl Z d dlZd dlZd dlZd dlZdZG dd dZe  d‘ ee y@e j	 
d‘Zedkr|e  d‘ e Ze ‘  ne Ze ‘  W nJ ek
rΌ   ed	 e  d
‘ e d‘ Y n ek
rΦ   ed Y nX dS )ι    Nu  [34m

βββββββ ββββββ   βββ βββββββ βββββββββ
ββββββββββββββ   βββββββββββββββββββββ
ββββββββββββββ   ββββββ   βββ   βββ   
βββββββ βββββββ βββββββ   βββ   βββ   
βββ     βββ βββββββ βββββββββ   βββ   
βββ     βββ  βββββ   βββββββ    βββ   
                                      
[31m[[37mAuthor: Akbar-Neotech[31m]
[37mc               @   s   e Zd Zdd ZdS )Ϊbukac                sό   t dd ‘ }tjd|d}| ‘ }td|d d d   td	|d d d
 d d |d d d
 d d |d d d
 d d f  td d| }| dd‘}| dd‘}dd dd  dd dd dd  fdd}||| d S ) Nzcfg.jsonΪrz0https://api.pivot.one/api/center/get_my_homepage)ΪurlΪdataz[32mUsername [31m: [37m%sr   ΪuserZnickzV[32mBalance  [31m: [33m- [37m%s PVT
	   [33m- [37m%s PVTP
	   [33m- [37m%s BTCZwalletr   Znumι   ι   z
		[1;30mMemulai.... 
[37mz $"ptypes": [1,2,3,4,10,20,30],%sϊ{Ϊ ϊ$c       	      S   sz   t jd| d}| ‘ }|j}t d|‘}t|}xDt|D ]8}|d d | d }tdd}| 	|d	 ‘ | 
‘  q:W d S )
Nz*https://api.pivot.one/api/post/favor_query)r   r   z"pid"(.*?)"r   ΪlistΪpidzcookies.datza+Ϊ
)ΪrequestsΪpostΪjsonΪtextΪreΪfindallΪlenΪrangeΪopenΪwriteΪclose)	ΪtZgfavorZjfavorZsfavorZliΪlΪxZpfavorΪfu© r   ϊbot.pyΪfavor   s    
zbuka.panggil.<locals>.favorc       	      S   sz   t jd| d}| ‘ }|j}t d|‘}t|}xDt|D ]8}|d d | d }tdd}| 	|d	 ‘ | 
‘  q:W d S )
Nz(https://api.pivot.one/api/post/big_query)r   r   z"pid"(.*?)"r   r   r   zcookies.datza+r   )r   r   r   r   r   r   r   r   r   r   r   )	r   ZgbigZjbigZsbigΪlibΪler   Zpbigr   r   r   r   Ϊbig&   s    
zbuka.panggil.<locals>.bigc       	      S   sz   t jd| d}| ‘ }|j}t d|‘}t|}xDt|D ]8}|d d | d }tdd}| 	|d	 ‘ | 
‘  q:W d S )
Nz*https://api.pivot.one/api/post/flash_query)r   r   z"pid"(.*?)"r   r   r   zcookies.datza+r   )r   r   r   r   r   r   r   r   r   r   r   )	r   ZgflashZjflashZsflashZlsZlesr   Zpflashr   r   r   r   Ϊflash1   s    
zbuka.panggil.<locals>.flashc       	      S   sz   t jd| d}| ‘ }|j}t d|‘}t|}xDt|D ]8}|d d | d }tdd}| 	|d	 ‘ | 
‘  q:W d S )
Nz)https://api.pivot.one/api/post/flag_query)r   r   z"pid"(.*?)"r   r   r   zcookies.datza+r   )r   r   r   r   r   r   r   r   r   r   r   )	r   ZgflagZjflagZsflagZlerZlerzr   Zpflagr   r   r   r   Ϊflag<   s    
zbuka.panggil.<locals>.flagc       	      S   sz   t jd| d}| ‘ }|j}t d|‘}t|}xDt|D ]8}|d d | d }tdd}| 	|d	 ‘ | 
‘  q:W d S )
Nz-https://api.pivot.one/api/post/discover_query)r   r   z"pid"(.*?)"r   r   r   zcookies.datza+r   )r   r   r   r   r   r   r   r   r   r   r   )	r   ZgdisZjdisZsdisZledZledsr   Zpdisr   r   r   r   ΪdiscoverG   s    
zbuka.panggil.<locals>.discoverc       	         sΖ   |   |  |  |  |  t dd ‘ }x|D ]}d||f }| dd‘}| dd‘}tjd|d}| ‘ }|d	 d
kr¬td t d‘ t	 
d‘ t ‘  q<td t d‘ q<W d S )Nzcookies.datr   z$"pid":"%s",%sr	   r
   r   z7https://api.pivot.one/api/read_mini/receive_read_reward)r   r   Ϊmsgz+Today's read reward limit has been reached.z8[35mTodays read reward limit has been reached.... [37mr   zrm -f cookies.datz[36mEnergy terkumpul.... [37m)r   Ϊ	readlinesΪreplacer   r   r   ΪprintΪtimeΪsleepΪosΪsystemΪsysΪexit)	r   ΪaZsdΪir   ZpiZpisZrewardZhs)r#   r&   r    r%   r$   r   r   ΪsaveR   s&    



zbuka.panggil.<locals>.save)r   Ϊreadr   r   r   r*   r)   )Ϊselfr1   ΪhΪinfr   Ϊfr   r3   r   )r#   r&   r    r%   r$   r   Ϊpanggil   s"    Lzbuka.panggilN)Ϊ__name__Ϊ
__module__Ϊ__qualname__r9   r   r   r   r   r      s   r   Ϊclearz./cookies.datTzcookies.datz%[31m
Menghentikan program..... [37mzrm -f cookies.datι   z/[31mFile  "cfg.json"  tidak ditemukan!!! [37m)r-   r   r   r+   r/   Ziconr   r.   r*   ΪpathΪexistsΪdirΪremoveZfakr9   ΪKeyboardInterruptr,   ΪFileNotFoundErrorr   r   r   r   Ϊ<module>   s$   (\



