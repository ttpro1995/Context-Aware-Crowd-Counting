from model import ContextualModule

def explore_contexture_module():
    contextual_module = ContextualModule(512, 512)
    # TODO: what is scales
    print(contextual_module.scales)



if __name__ == "__main__":
    explore_contexture_module()