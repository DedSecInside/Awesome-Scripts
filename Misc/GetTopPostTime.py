import requests
import time
from datetime import datetime,timedelta
import dateutil.parser
class GetTopPostTime():
    def set_info(self,parameters):
        """
        Set the info about a parameter

        Args:
            self: (todo): write your description
            parameters: (dict): write your description
        """
        self.access_token = parameters.get("access_token","")#add your access token
        self.no_of_days_from_now = parameters.get("no_of_days",7)
        self.since = parameters.get("since",str((datetime.now()-timedelta(days=self.no_of_days_from_now)).date()))
        self.upto = parameters.get("upto",str(datetime.now().date()-timedelta(1)))
        self.page_id = parameters.get("page_id",'508160905939091')  
        self.like_score = parameters.get('like_score', 2)
        self.comment_score = parameters.get('comment_score',3)
        self.share_score = parameters.get('share_score',4)
        self.reaction_score = parameters.get('reaction_score',1)
        self.max_post_score = 2000000000


    def get_all_posts_between_range(self):
        """
        Get all posts in the blog.

        Args:
            self: (todo): write your description
        """
        output_format="%Y-%m-%d"
        result = requests.get("https://graph.facebook.com/"+str(self.page_id)+"/feed?&access_token="+self.access_token+"&limit=100")
        posts = []
        no_of_iterations = 4
        loop_break = False
        while no_of_iterations > 0:
            if result.status_code == 200 and "data" in result.json() and result.json()["data"]:
                for single_post in result.json()["data"]:
                    created_date = dateutil.parser.parse(single_post["created_time"],fuzzy=True).strftime(output_format)
                    if created_date>self.upto:
                        continue
                    elif created_date>=self.since and created_date<=self.upto:
                        posts.append(single_post)
                    else:
                        loop_break = True
                        break
            if loop_break:
                break
            else:
                if "paging" in result.json() and "next" in result.json()["paging"]:
                    result = requests.get(result.json()["paging"]["next"])
                else:
                    break
            no_of_iterations-=1

        return posts

    def get_stats_for_each_post(self,result_posts):
        """
        Obtain the stats for a list of posts.

        Args:
            self: (todo): write your description
            result_posts: (str): write your description
        """
        max_count,time = 0,0
        top_posts,top_posts_ids = [],[]
        index = 0
        for each_post in result_posts:
            count = 0
            result = requests.get("https://graph.facebook.com/"+str(each_post["id"])+"/insights/post_impressions?&access_token="+self.access_token)
            if result.status_code == 200 and "data" in result.json() and result.json()["data"]:
                count+=result.json()["data"][0]["values"][0]["value"]
            result = requests.get("https://graph.facebook.com/"+str(each_post["id"])+"/insights/post_engagements?&access_token="+self.access_token)
            if result.status_code == 200 and "data" in result.json() and result.json()["data"]:
                count+=result.json()["data"][0]["values"][0]["value"]
            result = requests.get("https://graph.facebook.com/"+str(each_post["id"])+"/insights/post_consumptions_by_type_unique?access_token="+self.access_token)
            if result.status_code == 200 and "data" in result.json() and result.json()["data"]:
                if "other clicks" in result.json()["data"][0]["values"][0]["value"]:
                    count+=result.json()["data"][0]["values"][0]["value"]["other clicks"]
                if "link clicks" in result.json()["data"][0]["values"][0]["value"]:
                    count+=result.json()["data"][0]["values"][0]["value"]["link clicks"]
            top_posts.append((count,index))
            top_posts_ids.append(each_post["id"])
            index+=1
            if count>max_count:
                max_count = count
                time = each_post["created_time"]
        output = {}
        time_format = "%H:%M:%S"
        output["time"] = k=dateutil.parser.parse(time,fuzzy=True).strftime(time_format)
        days = {0:"munday",1:"tuesday",2:"wednesday",3:"thursday",4:"friday",5:"saturday",6:"sunday"}
        date_format = "%Y-%m-%d"
        date = dateutil.parser.parse(time,fuzzy=True).strftime(date_format)
        date = date.split("-")
        output["day"] = days[datetime(int(date[0]),int(date[1]),int(date[2])).weekday()]
        top_posts = sorted(top_posts)[-5:]
        final_result = []
        for each_post in top_posts:
            final_result.append(top_posts_ids[each_post[1]])
        result = self.get_full_details_of_ids(final_result)
        output["top_posts"] = result
        return output

    def get_full_details_of_ids(self,ids):
        """
        A method to get details about all posts.

        Args:
            self: (todo): write your description
            ids: (list): write your description
        """
        top_posts = []
        for post_id in ids:
            post_dictionary = {}
            post = requests.get("https://graph.facebook.com/"+str(post_id)+"/?fields=id,message,description,picture,created_time,type,attachments,link,permalink_url&access_token="+self.access_token).json()
            post_dictionary['page_id'] = self.page_id
            post_dictionary['page_name'] = self.page_id
            post_dictionary['page_url'] = 'https://www.facebook.com/'+str(self.page_id)
            post_dictionary['post_id'] = post_id
            post_dictionary['post_title'] = post['message'] if 'message' in post.keys() else "<No Message>"
            post_dictionary['post_description'] = post['description'] if 'description' in post.keys() else ""

            if 'attachments' in post.keys() and 'data' in post['attachments'] and post['attachments']['data'] and 'media' in post['attachments']['data'][0]:
                post_dictionary['post_image_url'] = post['attachments']['data'][0]['media']['image']['src']
            elif 'picture' in post.keys():
                post_dictionary['post_image_url'] = post['picture']
            else:
                post_dictionary['post_image_url'] = ""

            if post_dictionary['post_title'] == "<No Message>" and 'attachments' in post.keys() and 'data' in post['attachments'] and post['attachments']['data'] and 'title' in post['attachments']['data'][0]:
                post_dictionary['post_title'] = post['attachments']['data'][0]['title']
            post_dictionary['score'] = 0
                #post_dictionary['post_url'] = 'https://www.facebook.com/'+post['id']
            post_dictionary['post_url'] = post['link'] if 'link' in post else post['permalink_url'] #copying 3rd party link if not exists copying FB permalink

                #post_dictionary['source_url'] = urlparse(post['link']).netloc if 'link' in post else "" #we were storing only domain previously
            post_dictionary['source_url'] = post['permalink_url']
            post_dictionary['post_type'] = post['type']
            post_dictionary['FB_post_id'] = post_dictionary['post_id']
            post_dictionary['normalised_score'] = float('%.10f'%(post_dictionary['score']/self.max_post_score *100)) # Take upto 10 decimals
            top_posts.append(post_dictionary)
        return top_posts



    def get_result(self):
        """
        Returns a list of all posts.

        Args:
            self: (todo): write your description
        """
        result = self.get_all_posts_between_range()
        top_time = self.get_stats_for_each_post(result)
        return top_time
if __name__=="__main__":
    parameters = {

    }
    obj = GetTopPostTime()
    obj.set_info(parameters)
    result = obj.get_result()
    print(result)
