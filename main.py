##

"""

  """

##

import pandas as pd
from githubdata import GithubData
from mirutil.funcs import norm_fa_str as norm


repo_path = 'https://github.com/imahdimir/d-uniq-BaseTickers'
cur_module_repo = 'https://github.com/imahdimir/gov-d-uniq-BaseTickers'

btic = 'BaseTicker'

def main() :

  pass

  ##
  btick_repo = GithubData(repo_path)
  btick_repo.clone_overwrite_last_version()
  ##
  fpn = btick_repo.data_fps[0]
  df = pd.read_parquet(fpn)
  df = df.reset_index(drop = False)
  ##
  df = df[[btic]]
  ##
  df[btic] = df[btic].apply(norm)
  ##
  df = df.sort_values(btic)
  ##
  df = df.drop_duplicates()
  ##
  df.to_parquet(fpn)
  ##
  commit_msg = 'BaseTicker is an ordinary column now not an index one'
  commit_msg += f' by repo: {cur_module_repo}'
  btick_repo.commit_and_push_to_github_data_target(commit_msg)
  ##
  btick_repo.rmdir()

  ##

##
# noinspection PyUnreachableCode
def add_from_ifb_ipo_data() :
  pass
  ##
  ifb_ipo_repo_url = 'https://github.com/imahdimir/raw-d-IFB-IPOs'

  ##
  ifb_ipo_repo = GithubData(ifb_ipo_repo_url)
  ifb_ipo_repo.clone_overwrite_last_version()
  ##
  ifb_fpn = ifb_ipo_repo.dir / 'IFB-IPOs.xlsx'
  df0 = pd.read_excel(ifb_fpn)
  ##
  df0 = df0[['نام نماد']]
  df0['bt'] = df0['نام نماد']
  ##
  df0['bt'] = df0['bt'].apply(norm)
  ##
  df0['-1'] = df0['bt'].str[-1]
  ##
  df0['bt'] = df0['bt'].str[:-1]
  ##
  ptr = '\D+'
  df0['NotHasNum'] = df0['bt'].str.fullmatch(ptr)
  ##
  df1 = df0[~ df0['NotHasNum']]
  for _ , row in df1.iterrows() :
    print('"' + row['bt'] + '":"' + row['bt'][:-1] + '",')

  ##
  dct_man = {
      "پترول1"  : "پترول" ,
      "وخاور1"  : "وخاور" ,
      "کنور1"   : "کنور" ,
      "ثشرق1"   : "ثشرق" ,
      "شپدیس1"  : "شپدیس" ,
      "همراه1"  : "همراه" ,
      "وایران1" : "وایران" ,
      "پکویر1"  : "پکویر" ,
      }

  ##
  df0.loc[df0['NotHasNum'] , btic] = df0['bt']
  ##
  msk = ~ df0['NotHasNum']
  msk &= df0['bt'].isin(dct_man.keys())

  df0.loc[msk , btic] = df0['bt'].str[:-1]
  ##
  df1 = df0[[btic]]
  ##
  btick = GithubData(repo_path)
  btick.clone_overwrite_last_version()
  ##
  fpn = btick.data_fps[0]
  ##
  df = pd.read_parquet(fpn)
  ##
  df = df.reset_index()
  ##
  df = pd.concat([df , df1])
  ##
  df = df.drop_duplicates()
  ##
  df.to_parquet(fpn)
  ##
  commit_msg = 'added 4 BaseTickers from IFB IPOs data'
  btick.commit_and_push_to_github_data_target(commit_msg)
  ##
  btick.rmdir()
  ifb_ipo_repo.rmdir()

  ##

##

# noinspection PyUnreachableCode
if False :
  pass
  ##
  ptr = '\D+'
  msk = ~ df[btic].str.fullmatch(ptr)
  df1 = df[msk]
  ##
  ptr = '\D+'
  msk = ~ df[btic].str.fullmatch(ptr)
  msk &= df[btic].str[:-1].isin(df[btic])

  df1 = df[msk]
  # sxl(df1, 'df1.xlsx')
  # df = df[~ msk]
  ##
  ptr = r'.+' + r'ح'
  msk = df[btic].str.fullmatch(ptr)
  df1 = df[msk]
  ##
  ptr = r'ض' + '.+'
  msk = df[btic].str.fullmatch(ptr)
  df1 = df[msk]
  ##
  ptr = r'ج' + '.+'
  msk = df[btic].str.fullmatch(ptr)
  df1 = df[msk]

  ##