import bot
import random
class Command(object):

    def __init__(self):
        self.commands = {
            "start": self.start,
            "end": self.end,
            "lunch": self.lunch,
            "help": self.help,
            "how many": self.how_many,
            "who" : self.who,
            "delete": self.delete
        }
        self.started=False
        self.user = None
        self.list = list()
        self.group= list()
        self.groupi = list()

    def handle_command(self, user, command):
        #response = "<@" + user + ">: "
        self.user = user
        if command in self.commands:
            response = self.commands[command]()
        else:
            response = "Sorry I don't understand the command: " + command + ". " + self.help()

        return response
    '''
        This comand starts the boot
    '''
    def start(self):
        self.started=True
        response = "Ey! Who is going to have lunch out today? \n\n Lets start a poll"
        return response
    '''
    Lunch: puts the user in the list
    '''
    def lunch(self):
        if self.started:
            response = "<@" + self.user + ">:"
            if (self.list.count(self.user)==0):
                self.list.append(self.user)
                response += "You have been added to the list"
            else:
                response += "You are already in the list"

        else:
            response="The poll has not been started, type start to start it please"
        return response

    '''
        Return how many members are in the list
    '''
    def how_many(self):
        if self.started:
            if len(self.list)>0:
                return len(self.list)
            else:
                return "The list is empty"
        else:
            return "The poll has not been started, type start to start it please"

    '''
        Return who is in the list
    '''
    def who(self):
        response=""
        if (self.started):
            if len(self.list==0):
                return "The list is empty"
            else:
                for i in self.list:
                    response += "<@"+str(i)+">\n"
        else:
            response = "The poll has not been started, type start to start it please"
        return response

    '''
        Makes the groups and print them in the slack group
    '''
    def make_groups(self, list, ngroup, nmember,rest):
        response= "The fisrt member of the group is the leader, the groups are organised randomly \n"
        for i in range(ngroup):
            response += "The group "+ str(i+1) + "is: \n"
            if rest>0:
                number = random.randrange(len(list))
                # self.groupi.append(list[number])
                response += "<@" + list[number] + "> \n"
                list.remove(list[number])
                rest -=1
            for j in range(nmember):
                number=random.randrange(len(list))
                #self.groupi.append(list[number])
                response+= "<@"+list[number]+"> \n"
                list.remove(list[number])
            response+="\n\n"
            #self.group.insert(i,self.groupi)
            #self.groupi.clear()
        return response
    '''
        End the poll 
    '''
    def end(self):
        if self.started:
            if len(self.list)>0:
                response = "<@here> \n The poll has finished \n"
                #im.open
                listlen=len(self.list)
                self.started=False
                ngroups = listlen // 7
                if(( (listlen % 7) !=0 ) or  listlen < 7):
                    ngroups+=1
                nmembers=(listlen// ngroups)
                rest = (listlen % ngroups)
                response += self.make_groups(self.list, ngroups, nmembers,rest)
               # response+= self.group + "\n\n\n"
                '''for i in self.group:
                    #leader = self.leader(self.group[i])
                    #response+= "<@"+self.group[i][leader]+"> es el leader \n\n"
                    response+= "<@"+i+"> es el group \n\n"
                '''
            else:
                response= "The list is empty"
        else:
            response="The poll has not been started, type start to start please"

        response +="\n\n /foursquare lunch in Madrid"
#        for i in self.group:
#            response+= str(i)
        return response

    def delete(self):
        if(self.started):
            if (self.list.count(self.user)!=0):
                response= "You have been deleted from the list"
                self.list.remove(self.user)
            else:
                response= "Yo are not in the list"
        else:
            response = "The poll has not been started, type start to start please"
        return response

    def help(self):
        response = "Currently I support the following commands:\r\n"

        for command in self.commands:
            response += command + "\r\n"

        return response

    '''
    MEJORAS
    
        Call the Foursquare bot when the poll ends.
        Open a direct message to advise the leaders that they are the leaders and the members of their groups (im.open)
        Call the canal in order to advise every body of the results
        Add the possibility to have slash
        I try doing (TIEMPO)
        

    '''