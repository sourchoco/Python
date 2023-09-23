def preprocess_data(filename):
    processed = {}
    with open(filename) as file:
        # 입력 받은 JSON 파일을 불러와 loaded에 저장합니다.
        loaded = file.read()
        loaded_dict = json.loads(loaded)
        # JSON 형식의 데이터에서 영화와 사용자 정보를 하나씩 가져옵니다.
        for key, value in loaded_dict.items() :
            # processed 딕셔너리에 title을 키로, user를 값으로 저장합니다.
            processed[int(key)] = value


        return processed


def reformat_data(title_to_users):
    user_to_titles = {}
    # 입력받은 딕셔너리에서 영화와 사용자 정보를 하나씩 가져옵니다.
    for movie, customer in title_to_users.items() :
        # user_to_titles에 사용자 정보가 있을 경우 사용자의 영화 정보를 추가합니다. 이때 영화 정보는 리스트형으로 저장됩니다.
        for key in customer :
            if key in user_to_titles :
                user_to_titles[key] += [movie]
            
                
            # user_to_titles에 사용자 정보가 없을 경우 사용자 정보와 영화 정보를 추가합니다. 이때 영화 정보는 리스트형으로 저장됩니다. 
            else : user_to_titles[key] = [movie]

                
    
    return user_to_titles


def get_closeness(title_to_users, title1, title2):
    # title_to_users를 이용해 title1를 시청한 사용자의 집합을 저장합니다.
    title1_users = set(title_to_users[title1])
    # title_to_users를 이용해 title2를 시청한 사용자의 집합을 저장합니다.
    title2_users = set(title_to_users[title2])
    
    # 두 작품을 모두 본 사용자를 구합니다.
    both = len(title1_users & title2_users)
    # 두 작품 중 하나라도 본 사용자를 구합니다.
    either = len(title1_users | title2_users)

    return both/either


def predict_preference(title_to_users, user_to_titles, user, title):
    # user_to_titles를 이용해 user가 시청한 영화를 저장합니다.
    titles = user_to_titles[user]
    # get_closeness() 함수를 이용해 유사도를 계산합니다.
    closeness_list = []
    for titles_ran in titles :
        closeness = get_closeness(title_to_users, titles_ran , title)
        closeness_list.append(closeness)

    return sum(closeness_list) / len(closeness_list)