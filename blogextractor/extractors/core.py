
from blogextractor.extractors.topic import NairalandTopicExtractor
from blogextractor.extractors.forum import NairalandForumExtractor
from blogextractor.extractors.post import NairalandPostExtractor


# use a factory function to return the appropriate extractor class
def get_extractor(blog, type):
    if not blog:
        # TODO: throw an appropriate error or exception
        # e.g. value error
        return

    return {
        'nairaland':
            {
                'forum': NairalandForumExtractor,
                'topic': NairalandTopicExtractor,
                'post': NairalandPostExtractor
            }
    }[blog][type]

