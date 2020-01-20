def format_duration(seconds):
    Result=""
    if seconds==0:
        return "now"
    if seconds%31536000!=0 and seconds<=31536000:
        if seconds%86400!=0 and seconds<=86400:
            if seconds%3600!=0 and seconds<=3600:
                if seconds%60!=0 and seconds<=60:
                    if seconds==1:
                        Result=str(seconds)+" second"
                        return Result
                    else:
                        Result=str(seconds)+" seconds"
                        return Result
                else:
                    minutes=int(seconds/60)
                    seconds=seconds-(minutes*60)
                    if minutes==1 and seconds!=1 and seconds!=0:
                        Result=str(minutes)+" minute and "+str(seconds)+" seconds"
                    elif minutes!=1 and minutes!=0 and seconds==1:
                        Result=str(minutes)+" minutes and "+str(seconds)+" second"
                    elif minutes!=1 and seconds!=1 and minutes!=0 and seconds!=0:
                        Result=str(minutes)+" minutes and "+str(seconds)+" seconds"
                    elif minutes==1 and seconds==1:
                        Result=str(minutes)+" minute and "+str(seconds)+" second"
                    elif minutes==1 and seconds==0:
                        Result=str(minutes)+" minute"
                    else:
                        Result=str(minutes)+" minutes"
                    return Result
            else:
                hours=int(seconds/3600)
                minutes=int((seconds-(hours*3600))/60)
                seconds=int(((seconds-(hours*3600))-(minutes*60)))
                if hours==1 and minutes!=1 and seconds!=1 and minutes!=0 and seconds!=0:
                    Result=str(hours)+" hour"+", "+str(minutes)+" minutes and "+str(seconds)+" seconds"
                elif hours!=1 and minutes==1 and seconds!=1 and minutes!=0 and seconds!=0:
                    Result=str(hours)+" hours"+", "+str(minutes)+" minute and "+str(seconds)+" seconds"
                elif hours!=1 and minutes!=1 and seconds==1 and minutes!=0 and seconds!=0:
                    Result=str(hours)+" hours"+", "+str(minutes)+" minutes and "+str(seconds)+" second"
                elif hours!=1 and minutes!=1 and seconds!=1 and minutes!=0 and seconds!=0:
                    Result=str(hours)+" hours"+", "+str(minutes)+" minutes and "+str(seconds)+" seconds"
                elif hours==1 and minutes==1 and seconds==1:
                    Result=str(hours)+" hour"+", "+str(minutes)+" minute and "+str(seconds)+" second"
                elif hours==1 and minutes==1 and seconds!=1 and seconds!=0:
                    Result=str(hours)+" hour"+", "+str(minutes)+" minute and "+str(seconds)+" seconds"
                elif hours==1 and minutes!=1 and seconds!=1 and minutes!=0 and seconds!=0:
                    Result=str(hours)+" hour"+", "+str(minutes)+" minutes and "+str(seconds)+" seconds"
                elif hours!=1 and seconds!=1 and minutes==0 and seconds!=0:
                    Result=str(hours)+" hours"+" and "+str(seconds)+" seconds"
                elif hours==1 and seconds!=1 and minutes==0 and seconds!=0:
                    Result=str(hours)+" hour"+" and "+str(seconds)+" seconds"
                elif hours==1 and seconds==1 and minutes==0:
                    Result=str(hours)+" hour"+" and "+str(seconds)+" second"
                elif hours==1 and minutes!=1 and minutes!=0 and seconds==0:
                    Result=str(hours)+" hour"+" and "+str(minutes)+" minutes"
                elif hours!=1 and minutes==1 and seconds==0:
                    Result=str(hours)+" hours"+" and "+str(minutes)+" minute"
                elif hours!=1 and minutes!=1 and minutes!=0 and seconds==0:
                    Result=str(hours)+" hours"+" and "+str(minutes)+" minutes"
                elif hours==1 and minutes==0 and seconds==0:
                    Result=str(hours)+" hour"
                else:
                    Result=str(hours)+" hours"
                
                return Result
        else:
            days=int(seconds/86400)
            hours=int((seconds-(days*86400))/3600)
            minutes=int((((seconds-(days*86400))-hours*3600)/60))
            seconds=int((((seconds-(days*86400))-hours*3600)-minutes*60))
            if days==1 and hours!=1 and minutes!=1 and seconds!=1 and hours!=0 and minutes!=0 and seconds!=0:
                Result=str(days)+" day"+", "+str(hours)+" hours, "+str(minutes)+" minutes and "+str(seconds)+" seconds"
            elif days==1 and hours==1 and minutes!=1 and seconds!=1 and minutes!=0 and seconds!=0:
                Result=str(days)+" day"+", "+str(hours)+" hour, "+str(minutes)+" minutes and "+str(seconds)+" seconds"
            elif days==1 and hours!=1 and minutes==1 and seconds!=1 and hours!=0 and seconds!=0:
                Result=str(days)+" day"+", "+str(hours)+" hours, "+str(minutes)+" minute and "+str(seconds)+" seconds"
            elif days==1 and hours!=1 and minutes!=1 and seconds==1 and hours!=0 and minutes!=0:
                Result=str(days)+" day"+", "+str(hours)+" hours, "+str(minutes)+" minutes and "+str(seconds)+" second"
            elif days==1 and hours==1 and minutes==1 and seconds!=1 and seconds!=0:
                Result=str(days)+" day"+", "+str(hours)+" hour, "+str(minutes)+" minute and "+str(seconds)+" seconds"
            elif days==1 and hours==1 and minutes!=1 and seconds==1 and minutes!=0:
                Result=str(days)+" day"+", "+str(hours)+" hour, "+str(minutes)+" minutes and "+str(seconds)+" second"
            elif days==1 and hours==1 and minutes==1 and seconds==1:
                Result=str(days)+" day"+", "+str(hours)+" hour, "+str(minutes)+" minute and "+str(seconds)+" second"
            elif days==1 and hours==0 and minutes!=1 and seconds!=1 and minutes!=0 and seconds!=0:
                Result=str(days)+" day"+", "+str(minutes)+" minutes and "+str(seconds)+" seconds"
            elif days==1 and hours!=1 and minutes==0 and seconds!=1 and hours!=0 and seconds!=0:
                Result=str(days)+" day"+", "+str(hours)+" hours and "+str(seconds)+" seconds"
            elif days==1 and hours!=1 and minutes!=1 and seconds==0 and hours!=0 and minutes!=0:
                Result=str(days)+" day"+", "+str(hours)+" hours and "+str(seconds)+" minutes"
            elif days==1 and hours==1 and minutes==0 and seconds!=1 and seconds!=0:
                Result=str(days)+" day"+", "+str(hours)+" hour and "+str(seconds)+" seconds"
            elif days==1 and hours==1 and minutes!=1 and seconds==0 and minutes!=0:
                Result=str(days)+" day"+", "+str(hours)+" hour and "+str(minutes)+" minutes" 
            elif days==1 and hours==1 and minutes==1 and seconds==0:
                Result=str(days)+" day"+", "+str(hours)+" hour and "+str(minutes)+" minute"
            elif days==1 and hours==1 and minutes==0 and seconds==0:
                Result=str(days)+" day"+" and "+str(hours)+" hour"
            elif days==1 and hours==0 and minutes==0 and seconds==0:
                Result=str(days)+" day"
            elif days!=1 and hours==0 and minutes==0 and seconds==0 and days!=0:
                Result=str(days)+" days"
            elif days!=1 and hours==1 and minutes==0 and seconds==0 and days!=0:
                Result=str(days)+" days"+" and "+str(hours)+" hour"
            elif days!=1 and hours==1 and minutes==1 and seconds==0 and days!=0:
                Result=str(days)+" days"+", "+str(hours)+" hour and "+str(minutes)+" minute"
            elif days!=1 and hours==1 and minutes==1 and seconds==1 and days!=0:
                Result=str(days)+" days"+", "+str(hours)+" hour, "+str(minutes)+" minute and "+str(seconds)+" second"
            elif days!=1 and hours==1 and minutes==1 and seconds==1 and days!=0:
                Result=str(days)+" days"+", "+str(hours)+" hour, "+str(minutes)+" minute and "+str(seconds)+" second"
            elif days!=1 and hours!=1 and minutes==1 and seconds==1 and days!=0 and hours!=0:
                Result=str(days)+" days"+", "+str(hours)+" hours, "+str(minutes)+" minute and "+str(seconds)+" second"
            elif days!=1 and hours!=1 and minutes!=1 and seconds==1 and days!=0 and hours!=0 and minutes!=0:
                Result=str(days)+" days"+", "+str(hours)+" hours, "+str(minutes)+" minutes and "+str(seconds)+" second"
            elif days!=1 and hours!=1 and minutes!=1 and seconds!=1 and days!=0 and hours!=0 and minutes!=0 and seconds!=0:
                Result=str(days)+" days"+", "+str(hours)+" hours, "+str(minutes)+" minutes and "+str(seconds)+" seconds"
            elif days==1 and hours!=1 and minutes!=1 and seconds!=1 and hours!=0 and minutes!=0 and seconds!=0:
                Result=str(days)+" day"+", "+str(hours)+" hours, "+str(minutes)+" minutes and "+str(seconds)+" seconds"
            elif days==1 and hours!=1 and minutes==1 and seconds!=1 and hours!=0 and seconds!=0:
                Result=str(days)+" day"+", "+str(hours)+" hours, "+str(minutes)+" minute and "+str(seconds)+" seconds"
            elif days==1 and hours!=1 and minutes==1 and seconds==1 and hours!=0:
                Result=str(days)+" day"+", "+str(hours)+" hours, "+str(minutes)+" minute and "+str(seconds)+" second"
            elif days==1 and hours==1 and minutes!=1 and seconds==1 and minutes!=0:
                Result=str(days)+" day"+", "+str(hours)+" hour, "+str(minutes)+" minutes and "+str(seconds)+" second"
            elif days!=1 and hours==1 and minutes==1 and seconds==1 and days!=0:
                Result=str(days)+" days"+", "+str(hours)+" hour, "+str(minutes)+" minute and "+str(seconds)+" second"
            elif days!=1 and hours==1 and minutes!=1 and seconds==1 and days!=0 and minutes!=0:
                Result=str(days)+" days"+", "+str(hours)+" hour, "+str(minutes)+" minutes and "+str(seconds)+" second"
            elif days!=1 and hours==1 and minutes!=1 and seconds!=1 and days!=0 and minutes!=0 and seconds!=0:
                Result=str(days)+" days"+", "+str(hours)+" hour, "+str(minutes)+" minutes and "+str(seconds)+" seconds"
            elif days==1 and hours==1 and minutes!=1 and seconds==1 and minutes!=0:
                Result=str(days)+" day"+", "+str(hours)+" hour, "+str(minutes)+" minutes and "+str(seconds)+" second"
            elif days!=1 and hours==1 and minutes!=1 and seconds==1 and days!=0 and minutes!=0:
                Result=str(days)+" days"+", "+str(hours)+" hour, "+str(minutes)+" minutes and "+str(seconds)+" second"
            elif days!=1 and hours!=1 and minutes!=1 and seconds==1 and days!=0 and hours!=0 and minutes!=0:
                Result=str(days)+" days"+", "+str(hours)+" hours, "+str(minutes)+" minutes and "+str(seconds)+" second"
            elif days==1 and hours!=1 and minutes!=1 and seconds==1 and hours!=0 and minutes!=0:
                Result=str(days)+" day"+", "+str(hours)+" hours, "+str(minutes)+" minutes and "+str(seconds)+" second"
            elif days!=1 and hours!=1 and minutes!=1 and seconds==0 and days!=0 and hours!=0 and minutes!=0:
                Result=str(days)+" days"+", "+str(hours)+" hours and "+str(minutes)+" minutes"
            elif days!=1 and hours!=1 and minutes==0 and seconds==0 and days!=0 and hours!=0:
                Result=str(days)+" days"+" and "+str(hours)+" hours"
            elif days!=1 and hours!=1 and minutes!=1 and seconds==1 and days!=0 and minutes!=0 and minutes!=0:
                Result=str(days)+" days"+", "+str(hours)+" hours and "+str(minutes)+" minutes"
            elif days!=1 and hours!=1 and minutes==1 and seconds!=1 and days!=0 and minutes!=0 and minutes!=0 and seconds!=0:
                Result=str(days)+" days"+", "+str(hours)+" hours, "+str(minutes)+" minute and "+str(seconds)+" seconds" 
            elif days!=1 and hours!=1 and minutes==0 and seconds!=1 and days!=0 and hours!=0 and seconds!=0:
                Result=str(days)+" days"+", "+str(hours)+" hours and "+str(seconds)+" seconds"
            elif days!=1 and hours==0 and minutes!=1 and seconds!=1 and days!=0 and minutes!=0 and seconds!=0:
                Result=str(days)+" days"+", "+str(minutes)+" minutes and "+str(seconds)+" seconds"
            return Result
    else:
        years=int(seconds/31536000)
        days=int((seconds-(years*31536000))/86400)
        hours=int(((seconds-(years*31536000))-days*86400)/3600)
        minutes=int((((seconds-(years*31536000))-days*86400)-hours*3600)/60)
        seconds=int((((seconds-(years*31536000))-days*86400)-hours*3600)-minutes*60)
        if years==1 and days!=1 and hours!=1 and minutes!=1 and seconds!=1:
            Result=str(years)+" year"+", "+str(days)+" days, "+str(hours)+" hours, "+str(minutes)+" minutes and "+str(seconds)+" seconds" 
            return Result
        elif years!=1 and days==1 and hours!=1 and minutes!=1 and seconds!=1:
            Result=str(years)+" years"+", "+str(days)+" day, "+str(hours)+" hours, "+str(minutes)+" minutes and "+str(seconds)+" seconds" 
            return Result
        elif years!=1 and days!=1 and hours==1 and minutes!=1 and seconds!=1:
            Result=str(years)+" years"+", "+str(days)+" days, "+str(hours)+" hour, "+str(minutes)+" minutes and "+str(seconds)+" seconds"
            return Result
        elif years!=1 and days!=1 and hours!=1 and minutes==1 and seconds!=1:
            Result=str(years)+" years"+", "+str(days)+" days, "+str(hours)+" hours, "+str(minutes)+" minute and "+str(seconds)+" seconds" 
            return Result
        elif years!=1 and days!=1 and hours!=1 and minutes!=1 and seconds==1:
            Result=str(years)+" years"+", "+str(days)+" days, "+str(hours)+" hours, "+str(minutes)+" minutes and "+str(seconds)+" second" 
            return Result
        elif days!=0 and hours!=0 and minutes!=0 and seconds!=0:
                Result=str(years)+" years"+", "+str(days)+" days, "+str(hours)+" hours, "+str(minutes)+" minutes and "+str(seconds)+" seconds" 
                return Result
        else:
            if days==0 and hours!=0 and minutes!=0 and seconds!=0:
                Result=str(years)+" years"+", "+str(hours)+" hours, "+str(minutes)+" minutes and "+str(seconds)+" seconds"
            elif days!=0 and hours==0 and minutes!=0 and seconds!=0:
                Result=str(years)+" years"+", "+str(days)+" days, "+str(minutes)+" minutes and "+str(seconds)+" seconds"
            elif days!=0 and hours!=0 and minutes==0 and seconds!=0:
                Result=str(years)+" years"+", "+str(days)+" days, "+str(hours)+" hours and "+str(seconds)+" seconds"
            elif days!=0 and hours!=0 and minutes!=0 and seconds==0:
                Result=str(years)+" years"+", "+str(days)+" days, "+str(hours)+" hours and "+str(minutes)+" minutes"
            elif days==0 and hours==0 and minutes!=0 and seconds!=0:
                Result=str(years)+" years"+", "+str(minutes)+" minutes and "+str(seconds)+" seconds"
            elif days==0 and hours!=0 and minutes==0 and seconds!=0:
                Result=str(years)+" years"+", "+str(hours)+" hours and "+str(seconds)+" seconds"
            elif days==0 and hours!=0 and minutes!=0 and seconds==0:
                Result=str(years)+" years"+", "+str(hours)+" hours and "+str(minutes)+" minutes"
            elif days==0 and hours==0 and minutes==0 and seconds!=0:
                Result=str(years)+" years and "+str(seconds)+" seconds"   
            else:
                Result=str(years)+" years" 
            return Result
        
if __name__=="__main__":
    print(format_duration(2507670))