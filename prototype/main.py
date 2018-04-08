from resume import Resume

if __name__ == '__main__':
    r = Resume()
    r.set_experience_info('2017', 'dalian')

    r_1 = r.clone()
    r_1.set_experience_info('2018', 'shanghai')

    r.display()
    r_1.display()
