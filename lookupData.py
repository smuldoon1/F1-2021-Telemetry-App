teamData = {0:{"name":"Mercedes", "colour":"#00D2BE"},
            1:{"name":"Ferrari", "colour":"#DC0000"},
            2:{"name":"Red Bull Racing", "colour":"#0600EF"},
            3:{"name":"Williams", "colour":"#005AFF"},
            4:{"name":"Aston Martin", "colour":"#006F62"},
            5:{"name":"Alpine", "colour":"#0090FF"},
            6:{"name":"Alpha Tauri", "colour":"#2B4562"},
            7:{"name":"Haas", "colour":"#FFFFFF"},
            8:{"name":"McLaren", "colour":"#FF8700"},
            9:{"name":"Alfa Romeo", "colour":"#900000"}}

def getTeamData(index):
    return teamData.get(index, {"name":"Unknown Team", "colour":"#CCCCCC"})

trackData = {0:{"circuit":"Albert Park Circuit", "location":"Melbourne", "country":"Australia"},
             1:{"circuit":"Circuit Paul Ricard", "location":"Le Castellet", "country":"France"},
             2:{"circuit":"Shanghai International Circuit", "location":"Shanghai", "country":"China"},
             3:{"circuit":"Bahrain International Circuit", "location":"Sakhir", "country":"Bahrain"},
             4:{"circuit":"Circuit de Barcelona-Catalunya", "location":"Barcelona", "country":"Spain"},
             5:{"circuit":"Circuit de Monaco", "location":"Monte Carlo", "country":"Monaco"},
             6:{"circuit":"Circuit Gilles Vileneuve", "location":"Montreal", "country":"Canada"},
             7:{"circuit":"Silverstone Circuit", "location":"Silverstone", "country":"United Kingdom"},
             8:{"circuit":"Hockenheimring", "location":"Hockenheim", "country":"Germany"},
             9:{"circuit":"Hungaroring", "location":"Budapest", "country":"Hungary"},
             10:{"circuit":"Circuit de Spa-Francorchamps", "location":"Spa-Francorchamps", "country":"Belgium"},
             11:{"circuit":"Autodromo Nazionale Monza", "location":"Monza", "country":"Italy"},
             12:{"circuit":"Marina Bay Street Circuit", "location":"Marina Bay", "country":"Singapore"},
             13:{"circuit":"Suzuka International Racing Course", "location":"Suzuka", "country":"Japan"},
             14:{"circuit":"Yas Marina Circuit", "location":"Yas Island", "country":"Abu Dhabi"},
             15:{"circuit":"Circuit of the Americas", "location":"Austin", "country":"United States"},
             16:{"circuit":"Autódromo José Carlos Pace", "location":"São Paulo", "country":"Brazil"},
             17:{"circuit":"Red Bull Ring", "location":"Spielberg", "country":"Austria"},
             18:{"circuit":"Sochi Autodrom", "location":"Sochi", "country":"Russia"},
             19:{"circuit":"Autódromo Hermanos Rodríguez", "location":"Mexico City", "country":"Mexico"},
             20:{"circuit":"Baku City Circuit", "location":"Baku", "country":"Azerbaijan"},
             21:{"circuit":"Bahrain International Circuit (Short)", "location":"Sakhir", "country":"Bahrain"},
             22:{"circuit":"Silverstone Circuit (Short)", "location":"Silverstone", "country":"Great Britain"},
             23:{"circuit":"Circuit of the Americas (Short)", "location":"Austin", "country":"United States"},
             24:{"circuit":"Suzuka International Racing Course (Short)", "location":"Suzuka", "country":"Japan"},
             25:{"circuit":"Hanoi Street Circuit", "location":"Hanoi", "country":"Vietnam"},
             26:{"circuit":"Circuit Zandvoort", "location":"Zandvoort", "country":"Netherlands"},
             27:{"circuit":"Autodromo Enzo e Dino Ferrari", "location":"Imola", "country":"Italy"},
             28:{"circuit":"Algarve International Circuit", "location":"Portimão", "country":"Portugal"},
             29:{"circuit":"Jeddah Corniche Circuit", "location":"Jeddah", "country":"Saudi Arabia"}}

def getTrackData(index):
    return trackData.get(index, {"name":"Unknown Track", "location":"Unknown City", "country":"Unknown Country"})

sessionTypes = {0:"Unknown Session Type",
               1:"Free Practice 1",
               2:"Free Practice 2",
               3:"Free Practice 3",
               4:"Short Practice",
               5:"Qualifying 1",
               6:"Qualifying 2",
               7:"Qualifying 3",
               8:"Short Qualifying",
               9:"One-Shot Qualifying",
               10:"Race",
               11:"Sprint Race",
               12:"Feature Race",
               13:"Time Trial Session"}

def getSessionType(type, formula):
    if formula == 2 and type == 10:
        return sessionTypes[12]
    sessionType = sessionTypes[type]
    return sessionType