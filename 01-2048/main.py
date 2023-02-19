# from dataclasses import dataclass, field

# background #bbada0

# empty #CCC0B4

# .tile.tile-2 .tile-inner {
#   background: #eee4da;
#   box-shadow: 0 0 30px 10px rgba(243, 215, 116, 0), inset 0 0 0 1px rgba(255, 255, 255, 0);
# }

# .tile.tile-4 .tile-inner {
#   background: #eee1c9;
#   box-shadow: 0 0 30px 10px rgba(243, 215, 116, 0), inset 0 0 0 1px rgba(255, 255, 255, 0);
# }

# .tile.tile-8 .tile-inner {
#   color: #f9f6f2;
#   background: #f3b27a;
# }

# .tile.tile-16 .tile-inner {
#   color: #f9f6f2;
#   background: #f69664;
# }

# .tile.tile-32 .tile-inner {
#   color: #f9f6f2;
#   background: #f77c5f;
# }

# .tile.tile-64 .tile-inner {
#   color: #f9f6f2;
#   background: #f75f3b;
# }

# .tile.tile-128 .tile-inner {
#   color: #f9f6f2;
#   background: #edd073;
#   box-shadow: 0 0 30px 10px rgba(243, 215, 116, 0.238095), inset 0 0 0 1px rgba(255, 255, 255, 0.142857);
#   font-size: 45px;
# }

# .tile.tile-256 .tile-inner {
#   color: #f9f6f2;
#   background: #edcc62;
#   box-shadow: 0 0 30px 10px rgba(243, 215, 116, 0.31746), inset 0 0 0 1px rgba(255, 255, 255, 0.190476);
#   font-size: 45px;
# }

# .tile.tile-512 .tile-inner {
#   color: #f9f6f2;
#   background: #edc950;
#   box-shadow: 0 0 30px 10px rgba(243, 215, 116, 0.396825), inset 0 0 0 1px rgba(255, 255, 255, 0.238095);
#   font-size: 45px;
# }

# @media screen and (max-width: 520px) {
#   .tile.tile-512 .tile-inner {
#     font-size: 25px;
#   }
# }

# .tile.tile-1024 .tile-inner {
#   color: #f9f6f2;
#   background: #edc53f;
#   box-shadow: 0 0 30px 10px rgba(243, 215, 116, 0.47619), inset 0 0 0 1px rgba(255, 255, 255, 0.285714);
#   font-size: 35px;
# }

# @media screen and (max-width: 520px) {
#   .tile.tile-1024 .tile-inner {
#     font-size: 15px;
#   }
# }

# .tile.tile-2048 .tile-inner {
#   color: #f9f6f2;
#   background: #edc22e;
#   box-shadow: 0 0 30px 10px rgba(243, 215, 116, 0.555556), inset 0 0 0 1px rgba(255, 255, 255, 0.333333);
#   font-size: 35px;
# }

# @media screen and (max-width: 520px) {
#   .tile.tile-2048 .tile-inner {
#     font-size: 15px;
#   }
# }

# .tile.tile-super .tile-inner {
#   color: #f9f6f2;
#   background: #3c3a33;
#   font-size: 30px;
# }

def main():
    while True:
        init_game()
        while True:
            spawn_tile()
            display_game()
            if game_over():
                break
            while not valid_direction():
                if restart():
                    break
                get_direction()
            else:
                swipe()
        alert_death()
        restart_game()            

if __name__ == "__main__":
    main()