def get_query():
    query = {
    "_source": [
        "text",
        "extended_tweet.full_text",
        "quoted_status.text",
        "quoted_status.extended_tweet.full_text"
    ],
    "query": {
        "bool": {
        "filter": [
            {
            "bool": {
                "must_not": {
                "exists": {
                    "field": "embedding.use_large.primary"
                  }
                }
              }
            },
            {
            "bool": {
                "must_not": {
                "exists": {
                    "field": "retweeted_status.id"
                  }
                }
              }
            }
          ]
        }
      }
    }
    return query

def get_tweet_text(hit):
    text = hit["extended_tweet"]["full_text"] if "extended_tweet" in hit else hit["text"]
    quoted_text = None
    if "quoted_status" in hit:
        quoted_status = hit["quoted_status"]
        quoted_text = quoted_status["extended_tweet"]["full_text"] if "extended_tweet" in quoted_status else quoted_status["text"]

    return text, quoted_text